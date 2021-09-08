from sqlite3.dbapi2 import Connection
from typing import List

from youtube.channel import Channel


def store_channels(con: Connection, channels: List[Channel]):
    cur = con.cursor()

    for channel in channels:
        params = (channel.id, channel.title, channel.description, channel.url,
                  channel.query, channel.base64_img)
        cur.execute('INSERT INTO channel VALUES (?, ?, ?, ?, ?, ?)', params)

    con.commit()

    cur.close()


def list_channels(con: Connection) -> List[Channel]:
    cur = con.cursor()

    channels = []

    query_result = cur.execute(
        'SELECT id, title, description, url, query, base64_img FROM channel ORDER BY title')

    for row in query_result:
        channels.append(Channel(
            id=row[0],
            title=row[1],
            description=row[2],
            url=row[3],
            query=row[4],
            base64_img=row[5]
        ))

    con.commit()

    cur.close()

    return channels
