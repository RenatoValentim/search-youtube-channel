from typing import Dict, List

import requests

from youtube.channel import Channel, create_channel
from youtube.youtube import YOUTUBE_URL, get_page_data


def search(keyword: str) -> List[Dict]:
    url = f'{YOUTUBE_URL}/results'
    html_page = requests.get(url, params={'search_query': keyword}).text
    data = get_page_data(html_page)
    contents = data['contents']['twoColumnSearchResultsRenderer']['primaryContents'][
        'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

    renderers = []

    for content in contents:
        if 'channelRenderer' in content:
            renderer = content['channelRenderer']
            renderer['keyword'] = keyword
            channel = create_channel(renderer)
            renderers.append(channel)
            continue

        if 'videoRenderer' in content:
            # TODO: Aqui teria um tratamento do renderer de vídeo
            renderers.append(None)

    return renderers


def search_channels_by_keywords(keywords: List[str]) -> List[Channel]:
    all_channels = []
    for keyword in keywords:
        contents = search(keyword)
        all_channels.extend(list(filter(
            lambda content: type(content) is Channel, contents)))

    channels = []
    for channel in all_channels:
        if channel not in channels:
            channels.append(channel)

    return channels
