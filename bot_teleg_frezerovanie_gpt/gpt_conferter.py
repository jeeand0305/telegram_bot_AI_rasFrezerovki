from g4f.client import Client
import g4f, asyncio, time

# reсquest= input("Задайте ваш вопрос : ")

async def gpt3_text(reсquest_me):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": reсquest_me}],
        stream=True
    )
    # asyncio.sleep(1)
    print(type(response))
    for respon in response:
        print(type(respon))
        # asyncio.sleep(1)
        print(respon)
        responce_text = respon
    time.sleep(1)
    return responce_text
        # await responce_text
        # if responce_text==None:
        #     time.sleep(1)
        #     print(None)
        #     await None
# бот работает нужно прикрутить в

print(asyncio.run(gpt3_text("csm ")))


# __________________________________________________________

# _providers = [
#     g4f.Provider.Aichat,
#     g4f.Provider.ChatBase,
#     g4f.Provider.Bing,
#     g4f.Provider.GptGo,
#     g4f.Provider.You,
#     g4f.Provider.Yqcloud,
# ]


# async def run_provider(provider: g4f.Provider.BaseProvider):
#     try:
#         response = await g4f.ChatCompletion.create_async(
#             model=g4f.models.default,
#             messages=[{"role": "user", "content": vopros}],
#             provider=provider,
#         )
#         print(f"{provider.__name__}:", response)
#     except Exception as e:
#         print(f"{provider.__name__}:", e)
#
#
# async def run_all():
#     calls = [
#         run_provider(provider) for provider in _providers
#     ]
#     await asyncio.gather(*calls)


# asyncio.run(run_all())

# __________________________________________________________________________

# class Anliz_message_responce_gpt():
#     """обрботка входящих всех сообщений
#      1. С ForMeMessage.get_request_message_for_me берем
#       ключь с сообщением
#      2. здесь его открываем даем gpt его ответ формируем
#       3. анлиз сообщений на которых была реакция чтобы неотвечать на сообщения
#       4. работа с картинками тоже через gpt"""
#     def __init__(self, recquest_me):
#         self.reсquest_me = recquest_me
#         self.responce_text = ""
#
#
#     def gpt3_text(self):
#         if self.reсquest_me:
#             response = g4f.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[{"role": "user", "content": self.reсquest_me}],
#                 stream=True
#             )
#             # print(type(response))
#             for respon in response:
#                 # print(type(respons))
#                 print(respon)
#             self.responce_text = respon
#             return self.responce_text
#         elif None:
#             return None
#
#
# AnalizMessage = Anliz_message_responce_gpt(recquest_me=vopros)
#
# AnalizMessage.gpt3_text()
#


# client = Client()