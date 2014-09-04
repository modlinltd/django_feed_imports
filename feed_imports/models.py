from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import utils


class FeedSource(models.Model):
    feed_name = models.CharField(max_length=255, blank=False, null=False,
                                 verbose_name=_('Feed Name'))
    language = models.CharField(max_length=8, choices=settings.LANGUAGES,
                                default='en', verbose_name=_('Language'))
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))
    url = models.CharField(max_length=255, blank=False, null=False,
                           verbose_name=_('URL'))

    def __unicode__(self):
        return self.feed_name

    def imported_items_count(self):
        return self.saved_items.count()

    def import_feed_items(self):
        utils.import_feed_items(self)


class FeedItem(models.Model):
    class Meta:
        ordering = ['-creation_time']

    title = models.CharField(max_length=255, blank=False, null=False,
                             verbose_name=_('Title'))
    content = models.TextField(blank=True, null=False,
                               verbose_name=_('Contents'))
    link = models.CharField(max_length=255, blank=True, null=True,
                            verbose_name=_('Link'))
    feed = models.ForeignKey(FeedSource, related_name='saved_items')

    creation_time = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateTimeField()

    @models.permalink
    def get_absolute_url(self):
        return ('feed_item', [self.pk])
