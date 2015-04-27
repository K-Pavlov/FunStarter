# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_service', '0005_auto_20150406_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='category',
            new_name='like',
        ),
        migrations.AddField(
            model_name='picture',
            name='like',
            field=models.ForeignKey(related_name=b'pictures', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Like', null=True, verbose_name=b'Picture'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='like',
            field=models.ForeignKey(related_name=b'stories', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Like', null=True, verbose_name=b'Story'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='picture',
            name='category',
            field=models.ForeignKey(related_name=b'pictures', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Category', null=True, verbose_name=b'Category'),
        ),
        migrations.AlterField(
            model_name='story',
            name='category',
            field=models.ForeignKey(related_name=b'stories', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Category', null=True, verbose_name=b'Category'),
        ),
    ]
