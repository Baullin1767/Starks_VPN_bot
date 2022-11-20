from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



button_change_link = KeyboardButton('/Изменить_пробную_ссылку')
button_delete_link = KeyboardButton('/Удалить')
button_cancel_change_link = KeyboardButton('/Отмена')


admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_keyboard.add(button_change_link).insert(button_delete_link).add(button_cancel_change_link)