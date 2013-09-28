from django.db import models
from django.conf import settings


class Wish(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL)

    src_url = models.URLField(blank=True, null=True)
    title = models.CharField(
        max_length=100, blank=True,
        null=True, db_index=True
    )
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to="/wishes/", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'wish'
        get_latest_by = "created"
        ordering = ['-created']

    def __unicode__(self):
        return "%s wish %s" % (self.account.get_full_name(), self.title)
