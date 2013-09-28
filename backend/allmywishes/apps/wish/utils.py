import urlparse
import logging
from django.core.files.base import ContentFile

import requests

from django.conf import settings

logger = logging.getLogger(__name__)


def get_wish_data(url):
    """
        returns None if some error occurred;
        returns dict with data:
        {
            "title": "title",
            "description": "description",
            "image": "src",
            "price": None
        }
    """
    payload = {
        'url': url,
        'token': settings.REDABILITY["API_TOKEN"]
    }
    readability_url = urlparse.urljoin(
        settings.REDABILITY["API_STARTPOINT"],
        settings.REDABILITY["API_PARSE_URL"]
    )
    response = requests.get(readability_url, params=payload)
    if response.status_code != requests.codes.ok:
        logger.error("Bad status code: %s" % response.status_code)
        return None
    item_data = response.json()
    actual_data = {
        "title": item_data["title"],
        "description": item_data["excerpt"],
        "image": item_data["lead_image_url"],
        "price": None
    }
    return actual_data


def fetch_image(url):
    """
        returns tuple: name, ContentFile instance
        or
        None if some error occurred!
    """
    try:
        fetch_data = requests.get(url)
    except requests.RequestException:
        logger.error("Incorrect url %s" % url)
        return None
    if fetch_data.headers['content-type'].split('/')[0] != 'image':
        logger.error("Seems it's not image %s" % url)
        return None
    name = urlparse.urlparse(url).path.split('/')[-1]
    return name, ContentFile(fetch_data.content)
