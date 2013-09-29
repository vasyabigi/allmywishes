import urlparse
import logging

from django.conf import settings
from django.core.files.base import ContentFile
from django.template.defaultfilters import truncatechars

import requests
from embedly import Embedly


logger = logging.getLogger(__name__)


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


class EmbedlyParser(object):

    def __init__(self, url):
        self.url = url
        client = Embedly(settings.EMBEDLY_API_KEY)
        self.obj = client.extract(self.url)

    def prepared_data(self):
        return {
            "title": truncatechars(self.obj["title"], 100),
            "description": self.obj["title"],
            "provider_name": self.obj["provider_name"],
            "image_src": self.get_main_image_src()

        }

    def get_main_image_src(self):
        images = [[x["url"], x["size"]] for x in self.obj["images"]]
        return max(images, key=lambda l: l[1])[0]

    def is_valid(self):
        return not bool(self.obj.get("error"))

    def errors(self):
        if not self.is_valid():
            return {
                "errors": "Provided url unreachable"
            }
        return None
