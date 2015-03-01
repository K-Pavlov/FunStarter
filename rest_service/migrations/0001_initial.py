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
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name=b'Name')),
            ],
            options={
                'db_table': 'category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', auto_now_add=True)),
                ('content', models.TextField(null=True, verbose_name=b'Content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User')),
            ],
            options={
                'db_table': 'comment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', auto_now_add=True)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User')),
            ],
            options={
                'db_table': 'like',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'200', null=True, verbose_name=b'Title')),
                ('image', models.ImageField(upload_to=b'', null=True, verbose_name=b'Image')),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.Category', null=True, verbose_name=b'Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User')),
            ],
            options={
                'db_table': 'picture',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'200', null=True, verbose_name=b'Title')),
                ('content', models.TextField(null=True, verbose_name=b'Content')),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.Category', null=True, verbose_name=b'Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User')),
            ],
            options={
                'db_table': 'story',
            },
            bases=(models.Model,),
        ),
    ]
