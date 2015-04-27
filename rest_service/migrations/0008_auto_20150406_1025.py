# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_service', '0007_auto_20150406_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='picture',
            field=models.ForeignKey(related_name=b'comments', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Picture', null=True, verbose_name=b'Picture'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='story',
            field=models.ForeignKey(related_name=b'comments', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='rest_service.Story', null=True, verbose_name=b'Story'),
            preserve_default=True,
        ),
    ]
