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
        "django.views",
        url(r"%s(?P<path>.*)$" % settings.STATIC_URL[1:], "static.serve", {
            "document_root": settings.STATIC_ROOT,
            'show_indexes': True,
            }),
        url(r"%s(?P<path>.*)$" % settings.MEDIA_URL[1:], "static.serve", {
            "document_root": settings.MEDIA_ROOT,
            'show_indexes': True,
            }),

        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    )
