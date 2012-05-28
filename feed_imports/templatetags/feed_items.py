from django import template
from django.conf import settings

from feed_imports.models import FeedSource

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_feed_items(context, name, limit=False):
    feed = None

    default_language = getattr(settings, 'DEFUALT_LANGUAGE', 'en')

    try:
        language = context['request'].LANGUAGE_CODE
    except KeyError:
        language = default_language  # Request not in context processor

    try:
        feed = FeedSource.objects.get(feed_name=name, language=language)
    except FeedSource.DoesNotExist:
        pass

    if not feed and language != default_language:
        try:
            feed = FeedSource.objects.get(feed_name=name,
                                          language=default_language)
        except FeedSource.DoesNotExist:
            pass

    if not feed:
        return None

    if limit:
        return feed.saved_items.all()[:limit]
    return feed.saved_items.all()
