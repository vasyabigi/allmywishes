from rest_framework import generics, permissions
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
        try:
            account = Account.objects.get(slug=self.kwargs.get("slug"))
        except Account.DoesNotExist:
            return []
        else:
            return self.queryset.filter(account=account).all()

    def pre_save(self, obj):
        if self.request.user.is_authenticated():
            #print self.get_serializer().__dict__
            #import ipdb; ipdb.set_trace()
            obj.account = self.request.user
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
