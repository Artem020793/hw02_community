# yatube_project
Социальная сеть блогеров
### Описание 
Yatube - это социальная сеть с авторизацией, персональными лентами, комментариями и подписками на авторов статей.
### Технологии
Python 3.7
Django 2.2.19
### Запуск проекта в dev-режиме
- Клонировать репозиторий:
- Перейти в папку с проектом:
- Установить виртуальное окружение для проекта:
```
python -m venv venv
``` 
- Активировать виртуальное окружение для проекта:
```
# для OS Lunix и MacOS
source venv/bin/activate

# для OS Windows
source venv/Scripts/activate
```
- Установить зависимости:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
- Выполнить миграции на уровне проекта:
```
cd yatube
python3 manage.py makemigrations
python3 manage.py migrate
```
- Запустить проект локально:
```
python3 manage.py runserver

# адрес запущенного проекта
http://127.0.0.1:8000
```
- Зарегистирировать суперпользователя Django:
```
python3 manage.py createsuperuser

# адрес панели администратора
http://127.0.0.1:8000/admin
```
### Авторы
Артем Римша
