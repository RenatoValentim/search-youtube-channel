import json
import re
from typing import Dict

from bs4 import BeautifulSoup

YOUTUBE_URL = 'https://www.youtube.com'
page_data_pattern = re.compile('var ytInitialData = (.*);')


def get_page_data(content: str) -> Dict:
    soup = BeautifulSoup(content, 'html.parser')

    for script in soup.find_all("script", {"src": False}):
        if script:
            match = page_data_pattern.search(script.string)
            if match is not None:
                return json.loads(match.group(1))
