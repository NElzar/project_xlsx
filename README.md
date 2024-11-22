## Kак развернуть проект?

* Клонируем проект удобным способом
* Копируем файл `.env.template` с корневой директории и в ней же создаем файл `.env` внутрь вставляя значение первого
* Запускаем команду `docker-compose up —build`
* Запускаем команду в одельном окне терминала `docker-compose exec web bash`
* Запускаем команду python manage.py migrate
* Ссылка на swagger http://localhost:8000/swagger/
* Post запрос для обработки xlsx файла http://localhost:8000/api/upload/
* Результат сохранения можно посмотреть в виде html тут http://localhost:8000/api/data/html/
* Результат сохранения можно посмотреть в виде json тут http://localhost:8000/api/data/json/


