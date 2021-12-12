from aiogram.types import reply_keyboard, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
button1 = KeyboardButton("Stocks")
button3 = KeyboardButton("/PER_ESR")
button4 = KeyboardButton("/PSR_PBR")
button9 = KeyboardButton('/Quit')
markup1 = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button3, button4, button9)

button5 = KeyboardButton('0.5')
button6 = KeyboardButton('1')
button7 = KeyboardButton("2")
button8 = KeyboardButton('5')

markup2 = ReplyKeyboardMarkup(resize_keyboard=True).row(button5, button6, button7,button8, button9)