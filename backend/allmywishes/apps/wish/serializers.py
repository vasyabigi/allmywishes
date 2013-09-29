from .models import Wish

from rest_framework import serializers


class WishSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Wish
        fields = ('id', 'title', 'description', 'price', 'created', 'image_url')

    def get_image_url(self, obj):
        if obj.image is not None:
            return obj.image.url
        return None
