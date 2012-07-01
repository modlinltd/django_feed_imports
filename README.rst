===================
django-feed-imports
===================

Import RSS and Atom feeds and save in the Django database.

Requirements
============

* Django >= 1.4
* Feedparser
* `django.core.context_processors.request` context processor (for the template
  tag usage)

Installation
============

Install from localshop::

    pip install django-feed-imports -i http://cheese.modlinltd.com/simple

Install from source with pip::

  pip install -e svn+ssh://code.modlinltd.com/modapps/django_feed_imports#egg=feed_imports

Or install from source:

    svn checkout svn+ssh://code.modlinltd.com/modapps/django_feed_imports
    cd django_feed_imports
    python setup.py install

Add it the application to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'feed_imports',
    )

Run `syncdb` and `migrate`::

    python manage.py syncdb
    python manage.py migrate

Usage
=====

#. Configure the feeds sources in the Admin.
#. Run the management command::

    python manage.py refresh_feeds

   *The management command should run as a cron job.*
#. Using the template tag::

    {% load feed_items %}
    {% get_feed_items "news" 5 as items %}
    {# Get the last 5 items from the feed "news" in the current language #}
    {% for item in items %} {# do stuff ... #} {% endfor %}

   The `get_feed_items` returns the last `n` items from the provided feed in
   the language as set in the request, with a fallback to the default language.

   If settings.DEFAULT_LANGUAGE is not defined, English will be assumed.

#. To use `feed_item.get_absolute_url()` you must the define a url with the
   name `feed_item` in you `urls.py`. For Example::

    url(r'^feed_item/(?P<pk>.+)$',
        login_required(DetailView.as_view(model=FeedItem)),
        name='feed_item'),
