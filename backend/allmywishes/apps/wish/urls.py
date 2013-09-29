from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from wish import views as wish_views


urlpatterns = format_suffix_patterns(patterns(
    'wish.views',

    url(r'^parse$', 'wish_parse', name='wish-parse'),

    url(r'^(?P<pk>\d+)$', wish_views.wish_retrieve_update_destroy, name='wish-retrieve-update-destroy'),
))
