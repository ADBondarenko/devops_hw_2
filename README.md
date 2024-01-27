# devops_hw_3
HSE Machine Learning and High Load Systems '25, DevOps, HW2

Автор: Artem Bondarenko, @ArBBBB

ТЗ: 
1.Используем репозиторий, в котором велась разработка REST API
2. Токен для телеграм бота передается через переменную окружения
BOT_TOKEN
3. Укажите в AnyTask ссылку на репозиторий
4. Укажите в AnyTask команду docker-compose run с необходимым
значением для переменной BOT_TOKEN

Успешного кодинга!
P.S. Если использовали хранилище для работы с данными, то его тоже
добавляем в docker-compose.yaml

Для запуска локально необходимо:
```
export BOT_TOKEN=<insert_token_here>
docker-compose up -- build
```
Бот доступен для тестирования по адресу:
```
https://t.me/dogs_api_test_bot
```
