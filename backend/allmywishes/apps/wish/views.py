from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from wish.utils import EmbedlyParser, fetch_image
from .models import Wish
from .serializers import WishSerializer
from .permissions import IsWishOwnerPermission
from accounts.models import Account


class WishListCreate(generics.ListCreateAPIView):
    model = Wish
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = (permissions.IsAuthenticated,)
    paginate_by = 10

    def get_queryset(self):
        return self.queryset.filter(account=self.request.user).all()

    def pre_save(self, obj):
        if self.request.user.is_authenticated():
            obj.account = self.request.user

    def post_save(self, obj, created):
        image_src = self.request.DATA.get("image")
        if image_src is not None:
            image_data = fetch_image(image_src)
            if image_data is not None:
                obj.image.save(*image_data)

wish_list_create = WishListCreate.as_view()


class WishRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    model = Wish
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = (IsWishOwnerPermission,)

wish_retrieve_update_destroy = WishRetrieveUpdateDestroy.as_view()


class WishRetrieve(generics.RetrieveAPIView):
    model = Wish
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        account = get_object_or_404(Account, slug=self.kwargs.get("slug"))
        return self.queryset.filter(account=account).all()

wish_retrieve = WishRetrieve.as_view()


class WishParse(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        """
        Return ferched data from provided url
        """
        url = request.GET.get("url")
        parser = EmbedlyParser(url)
        if parser.is_valid():
            return Response(parser.prepared_data())
        return Response(parser.errors(), status=404)

wish_parse = WishParse.as_view()


class WishDiscover(generics.ListAPIView):
    model = Wish
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = (permissions.IsAuthenticated,)
    paginate_by = 10

    def get_queryset(self):
        ids = self.request.GET.getlist("ids")
        friends_wishes = Wish.objects.filter(account__facebook_id__in=ids)
        if friends_wishes.exists():
            return friends_wishes
        account = self.request.user
        return Wish.objects.exclude(account=account).order_by("?")

wish_discover = WishDiscover.as_view()
