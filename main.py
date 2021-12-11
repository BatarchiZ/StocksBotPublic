import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import markup1, markup2
import functions as fn

API_TOKEN = "5091609282:AAHvExe0njoB95VSp3xyBSEqqPKh64xVi3I"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.DEBUG)

@dp.message_handler(commands=["start"])
async def send_info(message: types.Message):
    await message.answer("Hello "
                         "Commands:\n"
                         "/start  - Start Bot\n"
                         "/info   - Command Panel\n"
                         "/stocks - Get a stock market portfolio\n"
                         "/PER_ESR - Get a PER_ESR boxplot\n"
                         "/PSR_PBR -  Get a PSR_PBR boxplot\n"
                         "")


@dp.message_handler(commands=["info"])
async def send_info(message: types.Message):
    await message.answer('What should I do?', reply_markup=markup1)


@dp.message_handler(regexp="Stocks")
async def send_info(message: types.Message):
    await message.answer("Choose the standard deviation from the available range", reply_markup=markup2)

@dp.message_handler(commands=["PER_ESR"])
async def success(message: types.Message):
    print(message.message_id)
    await bot.send_photo(message.from_user.id, photo=open("PER_ESR_plots.jpeg", "rb"))

@dp.message_handler(commands=["PSR_PBR"])
async def success(message: types.Message):
    print(message.message_id)
    await bot.send_photo(message.from_user.id, photo=open("PSR_PBR_plots.jpeg", "rb"))





# @dp.message_handler(commands=["success"])
# async def success(message: types.Message):
#     print(message.message_id)
#     await bot.send_photo(message.from_user.id, photo=open("photo_2021-12-10_21-03-40.jpg", "rb"))

@dp.message_handler(regexp="[0-9]")
async def send_something(message: types.Message):
    import functions as fn
    data = fn.stonks(message.text)
    await message.answer(f"This is your personalised stock portfolio:\n\n{data}")

@dp.message_handler(commands=["p"])
@dp.message_handler(regexp=".")
async def send_something(message: types.Message):
    await message.answer("Try again")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


import functions as fn
print(fn.stonks(5))

