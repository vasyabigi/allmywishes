import urlparse
import logging

import requests
#from BeautifulSoup import BeautifulSoup as bs
#from readability.readability import Document

from django.conf import settings
from django.core.files.base import ContentFile
from django.template.defaultfilters import truncatechars

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


#class ParseWishItem(object):
#    """
#        Own parser need to be improved!
#    """
#
#    def __init__(self, url):
#        self.url = url
#        try:
#            self.fetched_data = requests.get(self.url)
#            self.content = self.fetched_data.content
#        except requests.RequestException:
#            logger.error("Incorrect url %s" % url)
#            assert False, "Provided url - unreachable!"
#
#    def get_title(self):
#        return Document(self.content).summary()
#
#    def get_description(self):
#        return Document(self.content).short_title()
#
#    def get_biggest_image(self):
#        """
#            making head requests for all images on page to find biggest one by
#            content length information in headers;
#            We believe it will not be background image :)
#        """
#        images_with_size = []
#        soup = bs(self.content)
#        for image in soup.findAll("img"):
#            name = image["src"].split("/")[-1]
#            if image["src"].lower().startswith("http") and not name.endswith("gif"):
#                src = image["src"].lower()
#                try:
#                    r = requests.head(src)
#                    size = int(r.headers['content-length'])
#                    print size
#                except requests.RequestException:
#                    pass
#                else:
#                    images_with_size.append(
#                        (src, size)
#                    )
#        # We believe it will not be background image :)
#        biggest_image = max(images_with_size, key=lambda x: x[1])
#        return biggest_image
#
#    def get_og_image(self):
#        pass
#
#    def get_price(self):
#        pass


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
