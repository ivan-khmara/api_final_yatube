# api_final
API для Yatube
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/ivan-khmara/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
## Примеры запросов к API.
### JWT-токен
Получение JWT-токена.
```
POST  /api/v1/jwt/create/
```
пример:
```
{
"username": "string",
"password": "string"
}
```
Обновление JWT-токена.
```
POST  /api/v1/jwt/refresh/
```
пример:
```
{
"refresh": "string"
}
```
Проверка JWT-токена.
```
POST  /api/v1/jwt/verify/
```
пример:
```
{
"token": "string"
}
```
### Публикации
Получение публикаций
```
GET  /api/v1/posts/
```
Создание публикации
```
POST  /api/v1/posts/
```
пример:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Получение публикации/Обновление публикации/Частичное обновление публикации
```
GET/PUT/PATCH  /api/v1/posts/{id}/
```
Удаление публикации
```
DELETE  /api/v1/posts/{id}/
```
### Комментарии
Получение комментариев
```
GET  /api/v1/posts/{post_id}/comments/
```
Создание комментария
```
POST  /api/v1/posts/{post_id}/comments/
```
пример:
```
{
"text": "string"
}
```
Создание комментария/Обновление комментария/Частичное обновление комментария
```
GET/PUT/PATCH   /api/v1/posts/{post_id}/comments/{id}/
```
Удаление комментария
```
DELETE  /api/v1/posts/{post_id}/comments/{id}/
```
### Подписки
Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
```
GET  /api/v1/follow/
```
Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса.
Анонимные запросы запрещены.
```
POST  /api/v1/follow/
```
пример:
```
{
"following": "string"
}
```
### Сообщества
Получение списка доступных сообществ и информации о сообществе
```
GET  /api/v1/groups/
GET  /api/v1/groups/{id}/
```