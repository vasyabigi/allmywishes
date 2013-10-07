from django.core.urlresolvers import reverse

from .models import Wish
from accounts.serializers import AccountPublicSerializer

from rest_framework import serializers
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.helpers import ThumbnailError


class WishMixin(object):
    def get_image_url(self, obj):
        try:
            image = get_thumbnail(obj.image, '400', quality=80)
        except ThumbnailError:
            return
        else:
            return image.url


class WishSerializer(WishMixin, serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    url = serializers.SerializerMethodField('get_wish_url')

    class Meta:
        model = Wish
        fields = ('id', 'title', 'description', 'created', 'image_url', 'url')

    def get_wish_url(self, obj):
        return reverse('wish-retrieve-update-destroy', kwargs={'pk': obj.pk})


class WishWithAccountSerializer(WishMixin, serializers.ModelSerializer):
    url = serializers.SerializerMethodField('get_wish_url')
    account = AccountPublicSerializer()
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Wish
        fields = ('id', 'title', 'description', 'created', 'image_url', 'account', 'url', 'slug')

    def get_wish_url(self, obj):
        return reverse('wish-retrieve', kwargs={'slug': obj.account.slug, 'pk': obj.pk})
