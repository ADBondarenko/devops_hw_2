# devops_hw_3
HSE Machine Learning and High Load Systems '25, DevOps, HW2

Автор: Artem Bondarenko, @ArBBBB

ТЗ: 

К нам обратился директор ветеринарной клиники и сказал:
"Клинике необходим микросервис для хранения и обновления информации для собак!". А теперь ещё и бот в Telegram.

Напишем обертку для реализованных методов и совместим два сервиса в одном контейнере docker compose.

Для запуска локально необходимо:
```
export BOT_TOKEN=<insert_token_here>
docker-compose up -- build
```
Бот доступен для тестирования по адресу:
```
https://t.me/dogs_api_test_bot
```