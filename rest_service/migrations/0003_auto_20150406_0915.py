# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_service', '0002_auto_20150301_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunStarterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LikedEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='like',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='funstarteruser',
            name='liked_entity',
            field=models.ForeignKey(related_name=b'users', on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.LikedEntity', null=True, verbose_name=b'Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='funstarteruser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='liked_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.LikedEntity', null=True, verbose_name=b'Entites'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='liked_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.LikedEntity', null=True, verbose_name=b'Entites'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='liked_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.LikedEntity', null=True, verbose_name=b'Entites'),
            preserve_default=True,
        ),
    ]
