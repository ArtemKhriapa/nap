# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-26 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_sent_at', models.DateTimeField(auto_now_add=True)),
                ('mail_to', models.EmailField(max_length=254)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sentemail',
            name='user',
        ),
        migrations.DeleteModel(
            name='SentEmail',
        ),
    ]