# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
        ('rest_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True, verbose_name=b'Content'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.Category', null=True, verbose_name=b'Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='title',
            field=models.CharField(max_length=b'200', null=True, verbose_name=b'Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.Category', null=True, verbose_name=b'Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='content',
            field=models.TextField(null=True, verbose_name=b'Content'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=b'200', null=True, verbose_name=b'Title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', auto_now_add=True),
        ),
    ]
