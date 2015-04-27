# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_service', '0004_auto_20150406_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', auto_now_add=True)),
                ('user', models.ForeignKey(related_name=b'likes', on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User')),
            ],
            options={
                'db_table': 'like',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='funstarteruser',
            name='liked_entity',
        ),
        migrations.RemoveField(
            model_name='funstarteruser',
            name='user',
        ),
        migrations.DeleteModel(
            name='FunStarterUser',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='liked_entity',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='liked_entity',
        ),
        migrations.RemoveField(
            model_name='story',
            name='liked_entity',
        ),
        migrations.DeleteModel(
            name='LikedEntity',
        ),
        migrations.AddField(
            model_name='comment',
            name='category',
            field=models.ForeignKey(related_name=b'comments', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Like', null=True, verbose_name=b'Comment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='category',
            field=models.ForeignKey(related_name=b'pictures', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Like', null=True, verbose_name=b'Picture'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(related_name=b'pictures', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User'),
        ),
        migrations.AlterField(
            model_name='story',
            name='category',
            field=models.ForeignKey(related_name=b'stories', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Like', null=True, verbose_name=b'Story'),
        ),
        migrations.AlterField(
            model_name='story',
            name='user',
            field=models.ForeignKey(related_name=b'stories', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'User'),
        ),
    ]
