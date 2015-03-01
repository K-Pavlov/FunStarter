from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

time_default = '2000-01-01 00:00'
class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100, null=True)

    class Meta:
        db_table = 'category'

class Story(models.Model):
    title = models.CharField(verbose_name='Title', max_length='200', null=True)
    content = models.TextField(verbose_name='Content', null=True)
    category = models.ForeignKey(Category, verbose_name='Category', blank=True,
                                null=True, default='', on_delete=models.SET_NULL)
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                            null=True, default='', on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)
     
    class Meta:
        db_table = 'story'

class Picture(models.Model):
    title = models.CharField(verbose_name='Title', max_length='200', null=True)
    image = models.ImageField(verbose_name='Image', null=True)
    category = models.ForeignKey(Category, verbose_name='Category', blank=True,
                                null=True, default='', on_delete=models.SET_NULL)
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                            null=True, default='', on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)

    class Meta:
        db_table = 'picture'

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                             null=True, default='', on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)
    content = models.TextField(verbose_name='Content', null=True)

    class Meta:
        db_table = 'comment'

# comments, stories and pictures can have likes
# so a polymorphic relationships between models is used
class Like(models.Model):
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                             null=True, default='', on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'like'