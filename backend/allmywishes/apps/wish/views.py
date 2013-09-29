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
        try:
            account = Account.objects.get(slug=self.kwargs.get("slug"))
        except Account.DoesNotExist:
            return []
        else:
            return self.queryset.filter(account=account).all()

    def pre_save(self, obj):
        if self.request.user.is_authenticated():
            obj.account = self.request.user


wish_list_create = WishListCreate.as_view()
