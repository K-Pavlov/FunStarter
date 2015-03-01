# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(related_name=b'likes', on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='category',
            field=models.ForeignKey(related_name=b'pictures', on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.Category', null=True, verbose_name=b'Category'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(related_name=b'pictures', on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User'),
        ),
        migrations.AlterField(
            model_name='story',
            name='category',
            field=models.ForeignKey(related_name=b'stories', on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.Category', null=True, verbose_name=b'Category'),
        ),
        migrations.AlterField(
            model_name='story',
            name='user',
            field=models.ForeignKey(related_name=b'stories', on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User'),
        ),
    ]
