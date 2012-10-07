# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sala'
        db.create_table('maint_sala', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('maint', ['Sala'])

        # Adding model 'Ponencia'
        db.create_table('maint_ponencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ponente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maint.Ponente'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('resumen', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('evento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maint.Evento'])),
            ('sala', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maint.Sala'])),
        ))
        db.send_create_signal('maint', ['Ponencia'])

        # Adding model 'Ponente'
        db.create_table('maint_ponente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('curriculum', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('maint', ['Ponente'])

        # Adding model 'Evento'
        db.create_table('maint_evento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('maint', ['Evento'])


    def backwards(self, orm):
        # Deleting model 'Sala'
        db.delete_table('maint_sala')

        # Deleting model 'Ponencia'
        db.delete_table('maint_ponencia')

        # Deleting model 'Ponente'
        db.delete_table('maint_ponente')

        # Deleting model 'Evento'
        db.delete_table('maint_evento')


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
        }
    }

    complete_apps = ['maint']