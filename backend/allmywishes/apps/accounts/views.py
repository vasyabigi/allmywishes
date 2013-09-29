from django.contrib import auth

from .models import Account
from .serializers import AccountInfoSerializer, AccountDetailSerializer

from rest_framework import generics, permissions, response, status


class AccountInfo(generics.GenericAPIView):
    model = Account
    permission_classes = (permissions.AllowAny,)
    serializer_class = AccountInfoSerializer

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return response.Response({"is_authenticated": False}, status=status.HTTP_200_OK)

        serializer = self.get_serializer(instance=self.request.user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

account_info = AccountInfo.as_view()


class AccountConnect(generics.GenericAPIView):
    model = Account
    permission_classes = (permissions.AllowAny,)
    serializer_class = AccountInfoSerializer

    def post(self, request, *args, **kwargs):
        # TODO: signedRequest
        serializer = self.get_serializer(data=request.DATA, files=request.FILES)
        facebook_id = request.DATA.get("facebook_id")

        if serializer.is_valid() and facebook_id:

            if not Account.objects.filter(facebook_id=facebook_id).exists():
                account = Account.objects.create_user(
                    facebook_id,
                    oauth_token=serializer.object.oauth_token,
                    name=serializer.object.name,
                    email=serializer.object.email,
                )
            else:
                account = Account.objects.filter(facebook_id=facebook_id).get()
                account.oauth_token = serializer.object.oauth_token
                account.name = serializer.object.name
                account.email = serializer.object.email
                account.save()

            account = auth.authenticate(
                oauth_token=serializer.object.oauth_token,
                facebook_id=facebook_id
            )

            auth.login(request, account)

            serializer = self.get_serializer(instance=account)

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

account_connect = AccountConnect.as_view()


class AccountLogout(generics.GenericAPIView):
    model = Account
    permission_classes = (permissions.AllowAny,)
    serializer_class = AccountInfoSerializer

    def get(self, *args, **kwargs):
        auth.logout(self.request)
        return response.Response({"is_authenticated": False}, status=status.HTTP_200_OK)

account_logout = AccountLogout.as_view()


class AccountDetails(generics.RetrieveAPIView):
    model = Account
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountDetailSerializer

account_details = AccountDetails.as_view()
