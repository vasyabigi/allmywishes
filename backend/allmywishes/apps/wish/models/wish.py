from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel


class Wish(TimeStampedModel, models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="wishes")

    src_url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to="wishes/", blank=True, null=True)

    class Meta:
        app_label = 'wish'
        get_latest_by = "created"
        ordering = ['-created']

    def __unicode__(self):
        return u"%s wish %s" % (self.account.get_full_name(), self.title)
