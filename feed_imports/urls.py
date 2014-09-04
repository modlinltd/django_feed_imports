from django.conf.urls import patterns, url
from django.views.generic import DetailView

from .models import FeedItem


urlpatterns = patterns('',
    url(r'^feed_item/(?P<pk>.+)$',
        DetailView.as_view(model=FeedItem),
        name='feed_item'),
)
