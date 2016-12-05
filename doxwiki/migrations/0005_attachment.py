# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import doxwiki.models


class Migration(migrations.Migration):

    dependencies = [
        ('doxwiki', '0004_auto_20161204_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=doxwiki.models.page_upload_path)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doxwiki.Page')),
            ],
        ),
    ]