# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0006_networkandsupport_background_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', markdownx.models.MarkdownxField()),
                ('content_en', markdownx.models.MarkdownxField(null=True)),
                ('content_de', markdownx.models.MarkdownxField(null=True)),
                ('content_es', markdownx.models.MarkdownxField(null=True)),
                ('content_fr', markdownx.models.MarkdownxField(null=True)),
                ('content_pt', markdownx.models.MarkdownxField(null=True)),
                ('content_ar', markdownx.models.MarkdownxField(null=True)),
                ('content_ja', markdownx.models.MarkdownxField(null=True)),
                ('content_zh_cn', markdownx.models.MarkdownxField(null=True)),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_de', models.CharField(max_length=255, null=True)),
                ('title_es', models.CharField(max_length=255, null=True)),
                ('title_fr', models.CharField(max_length=255, null=True)),
                ('title_pt', models.CharField(max_length=255, null=True)),
                ('title_ar', models.CharField(max_length=255, null=True)),
                ('title_ja', models.CharField(max_length=255, null=True)),
                ('title_zh_cn', models.CharField(max_length=255, null=True)),
                ('website', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('background_image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': '17 - Contact',
                'verbose_name_plural': '17 - Contact',
            },
        ),
    ]
