import os
import time

print("API Iniciada com sucesso!")
print(f"Conectando ao banco de dados em: {os.getenv('DB_HOST')}")
print(f"Usuário: {os.getenv('DB_USER')}")

# Simula uma conexão com o banco de dados
print("Conectado ao Banco de dados com sucesso!")

# Mantém o container rodando para o exercício
while True:
    time.sleep(1)
