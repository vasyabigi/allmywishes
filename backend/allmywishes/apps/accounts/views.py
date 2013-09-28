from .models import Account
from .serializers import AccountInfoSerializer

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
