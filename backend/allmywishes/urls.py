from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^ebat/', include(admin.site.urls)),

    url(r'^api/accounts/', include('accounts.urls')),
    url(r'^api/wishes/', include('wish.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns(
        "",
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    )
