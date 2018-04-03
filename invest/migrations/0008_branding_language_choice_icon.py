# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 00:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('invest', '0007_auto_20180309_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='branding',
            name='language_choice_icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]