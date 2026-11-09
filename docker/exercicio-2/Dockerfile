# Usa uma imagem base estável do Python
FROM python:3.11-alpine

# Define a pasta de trabalho dentro do contêiner
WORKDIR /app

# Copia primeiro o arquivo de requisitos para aproveitar o cache do Docker
COPY requirements.txt .

# Instala a biblioteca psycopg2 listada no arquivo de requisitos
RUN pip install --no-cache-dir -r requirements.txt

# Copia o script da nossa API para o contêiner
COPY app.py .

# Comando padrão para iniciar a aplicação
CMD ["python", "app.py"]
