from .models import Wish

from rest_framework import serializers


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ('id', 'title', 'description', 'image')
