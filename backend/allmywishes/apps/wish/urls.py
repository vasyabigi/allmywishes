from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns(patterns(
    'wish.views',

    url(r'^(?P<slug>[\w-]+)/$', 'wish_list_create', name='wish-list-create'),
))
