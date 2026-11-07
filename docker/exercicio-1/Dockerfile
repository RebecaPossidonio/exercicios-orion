# Usa uma iamgem base leve do Python (conforme pedido no exercício) 
FROM python:3.11-alpine

# Define a pasta onde as coisas vão acontecer dentro do container
WORKDIR /app

# Copia o nosso arquivo de código para dentro do container
COPY app.py .

# Comando que o Docker vai rodar para executar o nosso script
CMD ["python", "app.py"]
