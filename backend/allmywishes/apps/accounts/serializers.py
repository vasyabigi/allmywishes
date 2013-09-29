from .models import Account

from rest_framework import serializers


class AccountInfoSerializer(serializers.ModelSerializer):
    facebook_id = serializers.Field(source="facebook_id")
    is_authenticated = serializers.Field(source="is_authenticated")
    image = serializers.Field(source="get_avatar_url")

    class Meta:
        model = Account
        fields = ('id', 'name', 'email', 'is_authenticated', 'oauth_token', 'image', 'slug')


class AccountPublicSerializer(serializers.ModelSerializer):
    facebook_id = serializers.Field(source="facebook_id")
    image = serializers.Field(source="get_avatar_url")

    class Meta:
        model = Account
        fields = ('name', 'image', 'slug')


class AccountDetailSerializer(serializers.ModelSerializer):
    facebook_id = serializers.Field(source="facebook_id")
    image = serializers.Field(source="get_avatar_url")
    wishes = serializers.SerializerMethodField('get_wishes')

    class Meta:
        model = Account
        fields = ('name', 'image', 'slug', 'wishes')

    def get_wishes(self, obj):
        from wish.serializers import WishSerializer
        return WishSerializer(obj.wishes.all(), many=True)
