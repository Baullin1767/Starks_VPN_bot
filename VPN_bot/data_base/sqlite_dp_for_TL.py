import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('trial_link_db.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS menu(date_link TEXT PRIMARY KEY, trial_linck TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?)', tuple(data.values()))
        base.commit()