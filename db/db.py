import sqlite3
from sqlite3.dbapi2 import Connection


def create_all_tables(con: Connection):
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS channel 
                (id text, title text, description text, url text, query text, base64_img text)''')

    cur.close()


def init_db(db_name: str) -> Connection:
    con = sqlite3.connect(db_name)
    create_all_tables(con)

    return con
