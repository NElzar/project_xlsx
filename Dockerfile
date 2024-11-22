# Используем образ Python
FROM python:3.11

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Открываем порт для Django
EXPOSE 8000

# Команда для запуска встроенного сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
