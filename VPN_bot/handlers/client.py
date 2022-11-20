from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import yes_button, platforms, ready, help_and_platforms, platforms_

# Команда старт
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, "Привет это мой впн", reply_markup=yes_button)
        
# Выбор платформы
async def choose_platforms(message : types.Message):
    await bot.send_message(message.from_user.id, 'Сейчас тебе нужно выбрать платформу:', reply_markup=platforms)


# Перечень платформ

async def android(message : types.Message):
    await bot.send_message(message.from_user.id, 'Держи ссылку и скачивай приложение для использования. Нажми "Готово", как установишь.\n\n'+
'https://play.google.com/store/apps/details?id=org.outline.android.client', reply_markup=ready)

async def IOS(message : types.Message):
    await bot.send_message(message.from_user.id, 'Держи ссылку и скачивай приложение для использования. Нажми "Готово", как установишь.\n\n'+
'https://itunes.apple.com/us/app/outline-app/id1356177741', reply_markup=ready)

async def windows(message : types.Message):
    await bot.send_message(message.from_user.id, 'Держи ссылку и скачивай приложение для использования. Нажми "Готово", как установишь.\n\n'+
'https://raw.githubusercontent.com/Jigsaw-Code/outline-releases/master/client/stable/Outline-Client.exe', reply_markup=ready)

async def linux(message : types.Message):
    await bot.send_message(message.from_user.id, 'Держи ссылку и скачивай приложение для использования. Нажми "Готово", как установишь.\n\n'+
'https://raw.githubusercontent.com/Jigsaw-Code/outline-releases/master/client/stable/Outline-Client.AppImage', reply_markup=ready)

# Пробная ссылка
async def trial_link(message : types.Message):
    await bot.send_message(message.from_user.id, 'Держи ссылку для использования: тебе нужно пройти по ней и нажать "подключить это устройство"'+
    ', и потом нажать "добавить сервер"\n\n'+
'https://s3.amazonaws.com/outline-vpn/invite.html#ss%3A%2F%2FY2hhY2hhMjAtaWV0Zi1wb2x5MTMwNT'
+'pWcTJEZ1F1S210ejQ%40167.99.188.223%3A53948%2F%3Foutline%3D1', reply_markup=help_and_platforms)

# Выбор ещё одной платформы
async def choose_another_platforms(message : types.Message):
    await bot.send_message(message.from_user.id, 'Сейчас тебе нужно выбрать платформу:', reply_markup=platforms_)

# перечень платформ
async def android_(message : types.Message):
    await bot.send_message(message.from_user.id, 'Держи ссылку и скачивай приложение для использования. Нажми "Готово", как установишь.\n\n'+
'https://play.google.com/store/apps/details?id=org.outline.android.client', reply_markup=help_and_platforms)

async def IOS_(message : types.Message):
    await bot.send_message(message.from_user.id, 'Держи ссылку и скачивай приложение для использования. Нажми "Готово", как установишь.\n\n'+
'https://itunes.apple.com/us/app/outline-app/id1356177741', reply_markup=help_and_platforms)

async def windows_(message : types.Message):
    await bot.send_message(message.from_user.id, 'Держи ссылку и скачивай приложение для использования. Нажми "Готово", как установишь.\n\n'+
'https://raw.githubusercontent.com/Jigsaw-Code/outline-releases/master/client/stable/Outline-Client.exe', reply_markup=help_and_platforms)

async def linux_(message : types.Message):
    await bot.send_message(message.from_user.id, 'Держи ссылку и скачивай приложение для использования. Нажми "Готово", как установишь.\n\n'+
'https://raw.githubusercontent.com/Jigsaw-Code/outline-releases/master/client/stable/Outline-Client.AppImage', reply_markup=help_and_platforms)

async def helping(message : types.Message):
    await bot.send_message(message.from_user.id, 'Опиши проблему, мы скоро ответим.')

def register_hendlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(choose_platforms, commands=['Да'])
    dp.register_message_handler(android, commands=['Android'])
    dp.register_message_handler(IOS, commands=['IOS'])
    dp.register_message_handler(windows, commands=['Windows'])
    dp.register_message_handler(linux, commands=['Linux'])
    dp.register_message_handler(trial_link, commands=['Готово'])
    dp.register_message_handler(choose_another_platforms, commands=['Платформы'])
    dp.register_message_handler(helping, commands=['Поддержка'])
    dp.register_message_handler(android_, commands=['Android_'])
    dp.register_message_handler(IOS_, commands=['IOS_'])
    dp.register_message_handler(windows_, commands=['Windows_'])
    dp.register_message_handler(linux_, commands=['Linux_'])