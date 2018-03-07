# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormViewPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContactFormPage',
            fields=[
                ('formviewpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contact.FormViewPage')),
                ('heading', models.CharField(default='Contact Us', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('contact.formviewpage',),
        ),
        migrations.CreateModel(
            name='FeedbackFormPage',
            fields=[
                ('formviewpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contact.FormViewPage')),
                ('heading', models.CharField(default='Feedback', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('contact.formviewpage',),
        ),
        migrations.CreateModel(
            name='ReportIssueFormPage',
            fields=[
                ('formviewpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contact.FormViewPage')),
                ('heading', models.CharField(default='Report Issue', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('contact.formviewpage',),
        ),
    ]