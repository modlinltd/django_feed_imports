import feedparser

from datetime import datetime
from time import mktime


def import_feed_items(feed_source):
    print 'Parsing "{0}", language={1}'.format(feed_source.feed_name,
                                               feed_source.language)
    feed = feedparser.parse(feed_source.url)

    for item in feed['items']:
        title = item['title']

        # Content for atom feeds:
        content = '<br />'.join([c['value'] for c in item.get('content', [])])

        description = item.get('description', '')
        date = datetime.fromtimestamp(mktime(item['published_parsed']))
        link = item.get('link', '')

        #self.stdout.write(u'Title: "{0}"\n'.format(title))

        if feed_source.saved_items.filter(title=title, publication_date=date)\
                                  .exists():
            print 'Item already exists'
            continue

        feed_source.saved_items.create(title=title,
                                       content=content or description,
                                       link=link,
                                       publication_date=date)

        print 'Item saved'
