from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import home

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name="home"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
