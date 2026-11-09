import os
import time
import psycopg2

print("Iniciando verificação de conexão com o banco de dados...")

# Resgata as configurações que definimos no docker-compose.yml
DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "senha123")
DB_NAME = os.getenv("DB_NAME", "orion_db")

# Como o banco de dados pode demorar alguns segundos a mais para ligar do que a API,
# fazemos uma estrutura de repetição (loop) tentando se conectar até dar certo.
conn = None
for i in range(10):
    try:
        print(f"Tentativa {i+1}: Conectando ao Postgres em {DB_HOST}...")
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            dbname=DB_NAME
        )
        break  # Se conectou com sucesso, quebra o loop de tentativas
    except psycopg2.OperationalError as e:
        print("Banco de dados ainda inicializando, aguardando 3 segundos...")
        time.sleep(3)

if conn:
    print("Conexão REAL com o PostgreSQL estabelecida com sucesso!")
    
    # O cursor serve para podermos executar comandos SQL de verdade no banco
    cursor = conn.cursor()
    
    # 1. Cria uma tabela de teste se ela não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS acessos (
            id SERIAL PRIMARY KEY,
            data_acesso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            mensagem TEXT
        );
    """)
    
    # 2. Grava um dado real no banco para provar a persistência exigida
    cursor.execute(
        "INSERT INTO acessos (mensagem) VALUES (%s);",
        ("Registro gerado com sucesso de dentro do container Docker!",)
    )
    
    # Confirma as alterações no banco de dados (Commit do SQL)
    conn.commit()
    print("Tabela verificada e novo registro gravado com sucesso no PostgreSQL!")
    
    # Fecha o canal com o banco de dados com segurança
    cursor.close()
    conn.close()
else:
    print("Não foi possível conectar ao banco de dados após as tentativas.")

# Mantém o container ativo para o compose não ficar reiniciando em loop
print("Script finalizado. Mantendo o container ativo...")
while True:
    time.sleep(1)
