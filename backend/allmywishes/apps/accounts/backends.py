from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class FacebookBackend(ModelBackend):

    def authenticate(self, username=None, oauth_token=None, **kwargs):
        if not oauth_token:
            return

        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            user = None

        return user
