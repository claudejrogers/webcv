# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('website_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('middle_initial', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('lab', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('division', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('website', ['Author'])

        # Adding model 'Journal'
        db.create_table('website_journal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('website', ['Journal'])

        # Adding model 'Article'
        db.create_table('website_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('journal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Journal'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('volume', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_page', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('end_page', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('issue', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('website', ['Article'])

        # Adding model 'AuthorOrder'
        db.create_table('website_authororder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Author'])),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Article'])),
            ('author_number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('website', ['AuthorOrder'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('website_author')

        # Deleting model 'Journal'
        db.delete_table('website_journal')

        # Deleting model 'Article'
        db.delete_table('website_article')

        # Deleting model 'AuthorOrder'
        db.delete_table('website_authororder')


    models = {
        'website.article': {
            'Meta': {'ordering': "['year', 'journal', 'volume', 'issue']", 'object_name': 'Article'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['website.Author']", 'through': "orm['website.AuthorOrder']", 'symmetrical': 'False'}),
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