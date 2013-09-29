from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns(patterns(
    'wish.views',

    url(r'^parse$', 'wish_parse', name='wish-parse'),
))
