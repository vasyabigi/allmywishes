from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns(patterns(
    'wish.views',

    url(r'^parse$', 'wish_parse', name='wish-parse'),
    url(r'^mine$', 'wish_list_create', name='wish-list-create-mine'),
    url(r'^mine/(?P<pk>\d+)$', 'wish_retrieve_update_destroy', name='wish-retrieve-update-destroy'),
    url(r'^discover$', 'wish_discover', name='wish-discover'),
))
