# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FeedSource'
        db.create_table('feed_imports_feedsource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en', max_length=8)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('feed_imports', ['FeedSource'])

        # Adding model 'FeedItem'
        db.create_table('feed_imports_feeditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(related_name='saved_items', to=orm['feed_imports.FeedSource'])),
            ('creation_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('publication_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('feed_imports', ['FeedItem'])


    def backwards(self, orm):
        
        # Deleting model 'FeedSource'
        db.delete_table('feed_imports_feedsource')

        # Deleting model 'FeedItem'
        db.delete_table('feed_imports_feeditem')


    models = {
        'feed_imports.feeditem': {
            'Meta': {'object_name': 'FeedItem'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'saved_items'", 'to': "orm['feed_imports.FeedSource']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'feed_imports.feedsource': {
            'Meta': {'object_name': 'FeedSource'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'feed_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '8'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['feed_imports']
