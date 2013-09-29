from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns(patterns(
    'wish.views',

    url(r'^parse$', 'get_wish_data', name='get-wish-data'),
))
