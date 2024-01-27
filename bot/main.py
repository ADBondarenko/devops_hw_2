import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from pydantic import BaseModel
import os
import requests
import json

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=os.getenv('BOT_TOKEN'))
API_URL = os.getenv('API_URL')
API_URL = f"http://"+API_URL
# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

# Хэндлер на команду /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello, mr. CEO of a Dog Clinic! \n"
                         "Here is the list of availible commands: \n"
                         "/get_service_status -- checks whether the service is running \n"
                        "/post_timestamp -- checks whether the POST method is correct \n"
                        "/get_dog <kind> or <> -- looks for all dogs or some specific kind \n"
                        "/post_dog <name> <pk> <kind> -- adds a new dog to the family \n"
                        "/get_dog_by_pk <pk> -- looks for a specific dog in DB \n"
                        "/patch_dog_by_pk <pk> <name> <kind> -- updates dogs records \n"
                        "<kind> is an Enum and might be terrier, bulldog, dalmatian")
    
@dp.message(Command("get_service_status"))
async def get_service(message: types.Message):
    base_url = API_URL
    method_url = "/"
    #No payload for this request.
    
    request_url = base_url+method_url
    reply = requests.get(request_url).content

    reply_text = f"Ответ сервиса: {json.loads(reply)}"

    await message.reply(reply_text)

@dp.message(Command("post_timestamp"))
async def post_timestamp(message: types.Message):
    base_url = API_URL
    method_url = "/post"
    #No payload for this request.
    
    
    request_url = base_url+method_url
    reply = requests.post(request_url).content

    reply_text = f"Ответ сервиса: {json.loads(reply)}"

    await message.reply(reply_text)

@dp.message(Command("get_dog"))
async def get_dog(message: types.Message,
                   command : CommandObject):

    #No payload for this request.
    if command.args is None:
        base_url = API_URL
        method_url = "/dog"
        request_url = base_url+method_url
        reply = requests.get(request_url).content
        reply_text = f"Ответ сервиса: {json.loads(reply)}"
        
    else:
        try:
            args_list = command.args.split(" ", maxsplit=-1)
            if len(args_list) != 1:
                raise ValueError
            kind = args_list[0]
            if kind not in ["terrier", "bulldog", "dalmatian"]:
                raise ValueError
            
        # Если получилось меньше двух частей, вылетит ValueError
        except ValueError:
            await message.answer(
                "Ошибка: неправильный формат команды. Правильно:\n"
                "/get_dog <kind> или <> \n"
                "<kind> может быть terrier, bulldog, dalmatian"
            )
            return
        base_url = API_URL
        method_url = f"/dog?kind={kind}"
        request_url = base_url+method_url
        
        reply = requests.get(request_url+method_url).content
    
        reply_text = f"Ответ сервиса: {json.loads(reply)}"

    await message.reply(reply_text)
    
@dp.message(Command("post_dog"))
async def post_dog(message: types.Message,
                   command : CommandObject):

    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы:\n"
            "/post_dog <kind> или <> \n"
        )
        return
    try:
        args_list = command.args.split(" ", maxsplit = -1)
        if len(args_list) != 3:
            raise ValueError
        name = args_list[0]
        pk = args_list[1]
        kind = args_list[2]

        if kind not in ["terrier", "bulldog", "dalmatian"]:
            raise ValueError
        if type(int(pk)) is not int:
            raise ValueError

    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Правиль:\n"
            "/post_dog <name> <pk> <kind> \n"
            "<kind> может быть terrier, bulldog, dalmatian"
        )
        return
    base_url = API_URL
    method_url = f"/dog?name={name}&pk={pk}&kind={kind}"
    #Hardcoded payload
    
    request_url = base_url+method_url
    reply = requests.post(request_url).content

    reply_text = f"Ответ сервиса: {json.loads(reply)}"

    await message.reply(reply_text)
#requests.patch(url, params={key: value}, args)

@dp.message(Command("get_dog_by_pk"))
async def get_dog_by_pk(message: types.Message,
                   command : CommandObject):
    
    base_url = API_URL

    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы:\n"
            "/get_dog_by_pk <pk>"
        )
        return
    try:
        pk = command.args.split(" ", maxsplit = -1)
        if len(pk) != 1:
            raise ValueError
    
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Правильно:\n"
            "/get_dog_by_pk <pk>"
        )
        return
        
    pk = pk[0]
    method_url = f"/dog/{pk}"
    request_url = base_url+method_url
    reply = requests.get(request_url).content

    reply_text = f"Ответ сервиса: {json.loads(reply)}"

    await message.reply(reply_text)


@dp.message(Command("patch_dog_by_pk"))
async def patch_dog_by_pk(message: types.Message,
                   command : CommandObject):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы:\n"
            "/post_dog <pk> <name> <kind> \n"
            "<kind> может быть terrier, bulldog, dalmatian"
        )
        return
    try:
        args_list = command.args.split(" ", maxsplit = -1)
        if len(args_list) != 3:
            raise ValueError
        pk = args_list[0]
        name = args_list[1]
        kind = args_list[2]

        if kind not in ["terrier", "bulldog", "dalmatian"]:
            raise ValueError
        if type(int(pk)) is not int:
            raise ValueError

    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Правиль:\n"
            "/post_dog <pk> <name> <kind> \n"
            "<kind> может быть terrier, bulldog, dalmatian"
        )
        return
    base_url = API_URL
    method_url = f"/dog/{pk}?name={name}&kind={kind}"
    #Hardcoded payload
    
    request_url = base_url+method_url
    reply = requests.patch(request_url).content

    reply_text = f"Ответ сервиса: {json.loads(reply)}"

    await message.reply(reply_text)


if __name__ == "__main__":
    asyncio.run(main())




