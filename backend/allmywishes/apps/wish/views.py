from .models import Wish
from .serializers import WishSerializer
from accounts.models import Account

from rest_framework import generics, permissions


class WishListCreate(generics.ListCreateAPIView):
    model = Wish
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = (permissions.IsAuthenticated,)
    paginate_by = 10

    def get_queryset(self):
        account = Account.objects.get(slug=self.request.GET.get("slug")) if self.request.GET.get("slug") else self.request.user
        return self.queryset.filter(wishes__account=account).all()

wish_list_create = WishListCreate.as_view()
