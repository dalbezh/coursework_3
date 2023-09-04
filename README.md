# Movie Library API

#### Technology stack:
[![Python](https://img.shields.io/badge/python-v3.9-orange)](https://www.python.org/downloads/release/python-394/)
[![Flask](https://img.shields.io/badge/Flask-v2.2.2-blue)](https://flask.palletsprojects.com/en/2.3.x/changes/#version-2-2-2)
[![flask-restx](https://img.shields.io/badge/FlaskRESTX-v1.0.3-blue)](https://flask-restx.readthedocs.io/en/latest/index.html)
___
#### Краткое описание
API умеет отдавать из БД SQLite данные о фильмах, жанрах и режиссёрах. 
Реализована регистрация и аутентификация по JWT.
___
#### Локальный запуск и работа с приложением
Установка зависимостей
```shell
pip install -r requirements.txt
```
Запуск приложения
```shell
python main.py
```

http://localhost:5000

Посмотреть доступные роуты можно в Swagger`е:

http://localhost:5000/docs
___
#### Тесты
Добавлены тесты для сервисов DirectorService, GenreService и MovieService.  Используется pytest.
Для прогона нужно запустить в консоли:
```shell
pytest
```
___
#### По структуре и функционалу приложения
- [x]  Бизнес логика находится в [сервисах](./app/services)
- [x]  Присутствует слой [DAO](./app/dao) вокруг [моделей](./app/dao/model)
- [x]  В схемах присутствуют нужные поля и не отдаются пароли
- [x]  Коды ответов возвращаются согласно правилам REST
