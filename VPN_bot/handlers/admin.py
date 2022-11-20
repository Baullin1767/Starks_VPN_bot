from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot
from data_base.sqlite_dp_for_TL import sql_add_command
from keyboards import admin_kb

ID = None

class FSMAdmin(StatesGroup):
    date_link = State()
    trial_linck = State()

# Проверка на возможность управления ссылками
async def make_changes_command(message : types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Здравствуйте мистер или миссис Старк', reply_markup=admin_kb.admin_keyboard)
    await message.delete()



# Начало добавления пробной ссылки
async def tlc_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.date_link.set()
        await message.reply('Напиши дату ссылки')

# Отмена
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Хорошо, отменил')


# Записываем дату ссылки
async def set_date_linc(message: types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['date_link'] = message.text
        await FSMAdmin.next()
        await message.reply('Пришли пробную ссылку')

# Записываем ссылку
async def load_trial_link(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['trial_linck'] = message.text

        await sql_add_command(state)
        await state.finish()
        await message.reply('Всё записал')




# Регистрация хендреров
def register_hendlers_admin(dp : Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(tlc_start, commands=['Изменить_пробную_ссылку'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands=['Отмена'])
    dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state="*")
    dp.register_message_handler(set_date_linc, state=FSMAdmin.date_link)
    dp.register_message_handler(load_trial_link, state=FSMAdmin.trial_linck)
    