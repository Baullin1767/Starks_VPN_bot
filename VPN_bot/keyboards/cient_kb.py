from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиши
b1 = KeyboardButton('/Да')

b2 = KeyboardButton('/Android')
b3 = KeyboardButton('/IOS')
b4 = KeyboardButton('/Windows')
b5 = KeyboardButton('/Linux')

b6 = KeyboardButton('/Готово')

b7 = KeyboardButton('/Поддержка')
b8 = KeyboardButton('/Платформы')

b9 = KeyboardButton('/Android_')
b10 = KeyboardButton('/IOS_')
b11 = KeyboardButton('/Windows_')
b12 = KeyboardButton('/Linux_')

# Клавиатуры
yes_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
yes_button.add(b1)

platforms = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
platforms.add(b2).insert(b3).add(b4).insert(b5)

ready = ReplyKeyboardMarkup(resize_keyboard=True)
ready.add(b6)

help_and_platforms = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
help_and_platforms.add(b7).insert(b8)

platforms_ = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
platforms_.add(b9).insert(b10).add(b11).insert(b12)