from db.channel import list_channels, store_channels
from db.db import init_db
import sys

from utils.colors import BLUE, GREEN, ORANGE, PURPLE, RED, WHITE
from youtube.search import search_channels_by_keywords


def main():
    keywords = sys.argv[1:]
    if keywords == []:
        print('Digite uma palavra que deseja pesquisar.')
        return

    channels = search_channels_by_keywords(keywords)
    if channels == []:
        print('Nenhum canal encontrado na pesquisa.')
        return

    con = init_db('youtube.db')
    store_channels(con, channels)

    for channel in channels:

        print(f'{GREEN}ID do canal: {RED}{channel.id}')
        print(f'{GREEN}Titulo: {WHITE}{channel.title}')
        print(f'{GREEN}Descrição: {WHITE}{channel.description}')
        print(f'{GREEN}URL do canal: {BLUE}{channel.url}')
        print(f'{GREEN}Palavra usada na pesquisa: {WHITE}{channel.query}')
        print(
            f'{GREEN}Image do Perfil em base64: {PURPLE}{channel.base64_img[:10]}...')
        print(
            f'{ORANGE}#######################################################################')

    count = len(list_channels(con))
    if count == 1:
        print(f'{WHITE}{count} canal armazenado no banco')
    else:
        print(f'{WHITE}{count} canais armazenados no banco')


if __name__ == "__main__":
    main()
