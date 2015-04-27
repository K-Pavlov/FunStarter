# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_service', '0006_auto_20150406_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='like',
        ),
        migrations.RemoveField(
            model_name='story',
            name='like',
        ),
        migrations.AddField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(related_name=b'likes', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Comment', null=True, verbose_name=b'Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='picture',
            field=models.ForeignKey(related_name=b'likes', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Picture', null=True, verbose_name=b'Picture'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='story',
            field=models.ForeignKey(related_name=b'likes', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Story', null=True, verbose_name=b'Story'),
            preserve_default=True,
        ),
    ]
