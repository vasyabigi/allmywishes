from .models import Account

from rest_framework import serializers


class AccountInfoSerializer(serializers.ModelSerializer):
    facebook_id = serializers.Field(source="facebook_id")
    is_authenticated = serializers.Field(source="is_authenticated")

    class Meta:
        model = Account
        fields = ('id', 'name', 'email', 'is_authenticated', 'oauth_token')
