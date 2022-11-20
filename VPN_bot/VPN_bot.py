from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_dp_for_TL


async def on_startup(_):
    print('Бот онлайн')
    sqlite_dp_for_TL.sql_start()


from handlers import client, admin, other

client.register_hendlers_client(dp)
admin.register_hendlers_admin(dp)




executor.start_polling(dp, skip_updates=True, on_startup=on_startup)