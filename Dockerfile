# Используем официальный образ Python
FROM python:3.10

# Установка зависимостей
WORKDIR /code
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

WORKDIR /code/app
COPY ./app .

WORKDIR /code
COPY main.py .

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
