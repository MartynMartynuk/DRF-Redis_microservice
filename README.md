# DRF-Redis_microservice #
Программа реализует микросервис проверки анаграмы, добавления устройств в базу данных PostgreSQL

## Установка ##
Для корректной работы требуется наличие Python3, redis-server и PosttgreSQL. Для установки зависимостей Python удобно воспользоваться командой
```
pip install -r requirements.txt
```
## Запуск ##
Для запуска сервера из папки "drf_redis_microservice" выполнить команду:
```
./manage.py runserver
```
## Использование
### 1. API-сервис проверки анаграмы
Отправить 'POST' запрос на адрес "localhost/api/redis/", содержащий json выражение 
```
{
    "word_1": "<слово_1>",
    "word_2": "<слово_2>"
}
```
В ответ вернётся json выражение 
```
{'is_anagram': <true или false>, 'counter': "<значение счетчика>"}
```
Данный функционал описан в функции [redis_counter](https://github.com/MartynMartynuk/DRF-Redis_microservice/blob/master/drf_redis_microservice/microservice/views.py#:~:text=def-,redis_counter,-(request)%3A)

### 2. Добавление в БД 10-ти устройств и привязывание к 5-ти из них endpoint-ов
Отправить 'POST' запрос на адрес "localhost/api/devices/", содержащий json выражение 
```
{
    "add_10": "true"
}
```
В ответ вернётся статус запроса 201.

Во исполнение ТЗ реализовано единственным POST запросом (хотя я бы делал несколькими - сначала добавил 10 устройств через POST, потом добавил эндпоинты через PUT).
Функционал реализован в методе [create](https://github.com/MartynMartynuk/DRF-Redis_microservice/blob/master/drf_redis_microservice/microservice/views.py#:~:text=def-,create,-(self%2C%20request%2C%20*args)

### 3. Получение списка устройств без endpoint-отв, сгруппированного по типам устройств
Отправить 'GET' запрос на адрес "localhost/api/devices/", содержащий json выражение 
```
{
    "sort": "true"
}
```
В ответ вернётся список устройств без endpoint-отв, сгруппированный по типам устройств.








