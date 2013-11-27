# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DrinkIngredient'
        db.create_table('examples_drinkingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('examples', ['DrinkIngredient'])

        # Adding model 'Drink'
        db.create_table('examples_drink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('examples', ['Drink'])

        # Adding M2M table for field ingredients on 'Drink'
        m2m_table_name = db.shorten_name('examples_drink_ingredients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('drink', models.ForeignKey(orm['examples.drink'], null=False)),
            ('drinkingredient', models.ForeignKey(orm['examples.drinkingredient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['drink_id', 'drinkingredient_id'])


    def backwards(self, orm):
        # Deleting model 'DrinkIngredient'
        db.delete_table('examples_drinkingredient')

        # Deleting model 'Drink'
        db.delete_table('examples_drink')

        # Removing M2M table for field ingredients on 'Drink'
        db.delete_table(db.shorten_name('examples_drink_ingredients'))


    models = {
        'examples.drink': {
            'Meta': {'object_name': 'Drink'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['examples.DrinkIngredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'examples.drinkingredient': {
            'Meta': {'object_name': 'DrinkIngredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['examples']