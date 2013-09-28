from django.conf.urls import patterns, url

urlpatterns = patterns(
    'accounts.views',

    url(r'^info/', 'account_info', name="account-info"),
)
