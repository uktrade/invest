# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-10 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0007_auto_20180427_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', markdownx.models.MarkdownxField(help_text='Markdown input. Please refer to https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet for intructions. Images may be dragged and droped into the editor')),
                ('content_en', markdownx.models.MarkdownxField(help_text='Markdown input. Please refer to https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet for intructions. Images may be dragged and droped into the editor', null=True)),
                ('content_de', markdownx.models.MarkdownxField(help_text='Markdown input. Please refer to https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet for intructions. Images may be dragged and droped into the editor', null=True)),
                ('content_es', markdownx.models.MarkdownxField(help_text='Markdown input. Please refer to https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet for intructions. Images may be dragged and droped into the editor', null=True)),
                ('content_fr', markdownx.models.MarkdownxField(help_text='Markdown input. Please refer to https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet for intructions. Images may be dragged and droped into the editor', null=True)),
                ('content_pt', markdownx.models.MarkdownxField(help_text='Markdown input. Please refer to https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet for intructions. Images may be dragged and droped into the editor', null=True)),
                ('content_ar', markdownx.models.MarkdownxField(help_text='Markdown input. Please refer to https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet for intructions. Images may be dragged and droped into the editor', null=True)),
                ('content_ja', markdownx.models.MarkdownxField(help_text='Markdown input. Please refer to https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet for intructions. Images may be dragged and droped into the editor', null=True)),
                ('content_zh_cn', markdownx.models.MarkdownxField(help_text='Markdown input. Please refer to https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet for intructions. Images may be dragged and droped into the editor', null=True)),
            ],
            options={
                'verbose_name': '16 - Last Page',
                'verbose_name_plural': '16 - Last Page',
            },
        ),
    ]
