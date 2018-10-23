# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 08:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighbor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='business_email',
        ),
        migrations.RemoveField(
            model_name='business',
            name='neighbourhood',
        ),
        migrations.AddField(
            model_name='business',
            name='business_emails',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='business_name',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bbb', to=settings.AUTH_USER_MODEL),
        ),
    ]
