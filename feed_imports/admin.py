from django.contrib import admin

from models import FeedSource, FeedItem


class FeedSourceAdmin(admin.ModelAdmin):
    list_display = ('feed_name', 'language', 'url', 'enabled',
                    'imported_items_count', )
    readonly_fields = ('imported_items_count', )
    list_filter = ('feed_name', 'language', 'enabled', )


class FeedItemAdmin(admin.ModelAdmin):
    list_display = ('feed', 'title', 'link', )


admin.site.register(FeedSource, FeedSourceAdmin)
admin.site.register(FeedItem, FeedItemAdmin)
