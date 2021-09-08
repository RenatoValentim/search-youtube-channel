from dataclasses import dataclass
from typing import Dict

import requests

from youtube.base64_image import get_as_base64
from youtube.youtube import YOUTUBE_URL, get_page_data


@dataclass
class Channel:
    id: str
    title: str
    description: str
    url: str
    base64_img: str
    query: str

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, arg):
        return self.id == arg.id


def create_channel(content: Dict) -> Channel:
    id = content['channelId']
    keyword = content['keyword']
    url = f'{YOUTUBE_URL}/channel/{id}'
    html_page = requests.get(url).text
    data = get_page_data(html_page)
    header = data['header']['c4TabbedHeaderRenderer']
    metadata = data['metadata']['channelMetadataRenderer']
    microformat = data['microformat']['microformatDataRenderer']

    title = header['title']
    description = metadata['description']
    url = microformat['urlCanonical']
    profile_img_url = header['avatar']['thumbnails'][1]['url']
    base64_profile_image = get_as_base64(profile_img_url)

    channel = Channel(id=id, title=title,
                      description=description, url=url,
                      base64_img=base64_profile_image, query=keyword)
    return channel
