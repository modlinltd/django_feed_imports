from django.core.management.base import BaseCommand

from feed_imports.models import FeedSource


class Command(BaseCommand):
    help = 'Import all feeds.'

    def handle(self, *args, **options):
        for feed in FeedSource.objects.filter(enabled=True):
            feed.import_feed_items()
            print '=' * 50
