Task Management Application

Описание проекта
Это веб-приложение для управления задачами с возможностью создавать, редактировать, удалять и сортировать задачи.

Используемые технологии
Python: Основной язык программирования.
Django: Веб-фреймворк для разработки серверной части.
Django REST Framework (DRF): Для создания RESTful API.
HTML и Bootstrap: Для разработки фронтенда и адаптивного дизайна.
Docker: Для контейнеризации приложения.
Nginx: Веб-сервер для обработки запросов.


Установка и запуск проекта

1. Клонирование репозитория
git clone https://github.com/Bely515/diploma.git
cd diploma
cd todo_api
cd taskmanager

2. Установка зависимостей
Создайте и активируйте виртуальное окружение:
python -m venv venv
venv\Scripts\activate     # Windows

Установите зависимости из requirements.txt:
pip install -r requirements.txt


3. Применение миграций
python manage.py makemigrations
python manage.py migrate

4. Запуск сервера разработки
python manage.py runserver
Приложение будет доступно по адресу http://127.0.0.1:8000/

