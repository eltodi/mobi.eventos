# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stand'
        db.create_table('maint_stand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('dedicacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('localidad', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        ))
        db.send_create_signal('maint', ['Stand'])


    def backwards(self, orm):
        # Deleting model 'Stand'
        db.delete_table('maint_stand')


    models = {
        'maint.evento': {
            'Meta': {'object_name': 'Evento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'maint.ponencia': {
            'Meta': {'object_name': 'Ponencia'},
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maint.Evento']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ponente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maint.Ponente']"}),
            'resumen': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sala': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maint.Sala']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'maint.ponente': {
            'Meta': {'object_name': 'Ponente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'curriculum': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'maint.sala': {
            'Meta': {'object_name': 'Sala'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'maint.stand': {
            'Meta': {'object_name': 'Stand'},
            'dedicacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['maint']