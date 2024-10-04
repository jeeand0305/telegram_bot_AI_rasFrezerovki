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
        # print(type(respon))
        # asyncio.sleep(1)
        # print(respon)
        responce_text = respon
    time.sleep(1)
    return responce_text
        # await responce_text
        # if responce_text==None:
        #     time.sleep(1)
        #     print(None)
        #     await None
# бот работает нужно прикрутить в

print(asyncio.run(gpt3_text("Как стать разработчикам на питоне напиши все навыки ")))


# __________________________________________________________
