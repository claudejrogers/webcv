# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.date_published'
        db.add_column('website_article', 'date_published',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 2, 18, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.date_published'
        db.delete_column('website_article', 'date_published')


    models = {
        'website.article': {
            'Meta': {'ordering': "['year', 'journal', 'volume', 'issue']", 'object_name': 'Article'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Author']", 'through': "orm['website.AuthorOrder']", 'symmetrical': 'False'}),
            'date_published': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 2, 18, 0, 0)'}),
            'end_page': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'issue': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Journal']"}),
            'start_page': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'website.author': {
            'Meta': {'ordering': "['last_name', 'first_name', 'middle_initial']", 'object_name': 'Author'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'division': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'lab': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'middle_initial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'website.authororder': {
            'Meta': {'ordering': "['article', 'author_number']", 'object_name': 'AuthorOrder'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Article']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Author']"}),
            'author_number': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'website.journal': {
            'Meta': {'ordering': "['name']", 'object_name': 'Journal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['website']