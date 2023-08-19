# Тестовое задание от Kokoc Group
# Разворачивание
1. [Установить](https://docs.docker.com/compose/install/) Docker
2. [Установить](https://git-scm.com/downloads) Git
3. Клонировать репозиторий:
```no-highlight
git clone https://github.com/tarasenkoartemiy/kokoc-group-test-task.git
```
4. В корневой папке проекта создать файл `.env` и заполнить, используя `template.env`:
* Перенести значения из `template.env` в `.env`: 
  * POSTGRES_HOST
  * POSTGRES_PORT
  * DJANGO_SUPERUSER_USERNAME
  * DJANGO_SUPERUSER_PASSWORD
  * DJANGO_SUPERUSER_EMAIL
* Вписать свои значения:
  * SECRET_KEY
  * DEBUG
  * POSTGRES_DB
  * POSTGRES_USER
  * POSTGRES_PASSWORD
5. Из корневой папки проекта запустить сервисы:
```no-highlight
docker compose up
```
6. Открыть второе окно терминала и выполнить:
```no-highlight
docker exec -it django python manage.py createsuperuser --noinput
```
# Использование
1. Запустить сбор информации и валютах и их курсах:
```no-highlight
docker exec -it django python manage.py run_parse
```
2. К admin панели можно получить доступ тут:  
Использовать имя пользователя и пароль из `template.env`
```no-highlight
http://0.0.0.0:8000/admin/
```
3. Курсы валют в json можно получить тут:
```no-highlight
http://0.0.0.0:8000/api/v1/show_rates/
```
3. Отфильтровать по дате:
```no-highlight
http://0.0.0.0:8000/api/v1/show_rates/?date=YYYY-MM-DD
```