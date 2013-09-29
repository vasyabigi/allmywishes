from .models import Wish

from rest_framework import serializers


class WishSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Wish
        fields = ('id', 'title', 'description', 'created', 'image_url')

    def get_image_url(self, obj):
        if obj is not None and obj.image is not None:
            try:
                return obj.image.url
            except ValueError:
                pass

        return None
