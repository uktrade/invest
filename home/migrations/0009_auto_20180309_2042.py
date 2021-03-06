# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 20:42
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_homepage_sector_lead_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='how_we_help',
            field=wagtail.core.fields.StreamField((('items', wagtail.core.blocks.StructBlock((('icon', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock())))), ('page_link', wagtail.core.blocks.StructBlock((('page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()))))), blank=True),
        ),
    ]
