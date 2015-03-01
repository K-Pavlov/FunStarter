from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

class SerializableGenericRelation(GenericRelation):
    def __init__(self, to, **kwargs):
        return super(SerializableGenericRelation, self).__init__(to, **kwargs)

    def __str__(self):
        return ''

class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

# comments, stories and pictures can have likes
# so a polymorphic relationships between models is used
class Like(models.Model):
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                             null=True, default='', on_delete=models.SET_NULL,
                             related_name='likes')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.content_type + ' ' + self.time 

    class Meta:
        db_table = 'like'

class Story(models.Model):
    title = models.CharField(verbose_name='Title', max_length='200', null=True)
    content = models.TextField(verbose_name='Content', null=True)
    category = models.ForeignKey(Category, verbose_name='Category', blank=True,
                                null=True, default='', on_delete=models.SET_NULL,
                                related_name='stories')
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                            null=True, default='', on_delete=models.SET_NULL,
                            related_name='stories')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.title + ' ' + self.time
     
    class Meta:
        db_table = 'story'

class Picture(models.Model):
    title = models.CharField(verbose_name='Title', max_length='200', null=True)
    image = models.ImageField(verbose_name='Image', null=True)
    category = models.ForeignKey(Category, verbose_name='Category', blank=True,
                                null=True, default='', on_delete=models.SET_NULL,
                                related_name='pictures')
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                            null=True, default='', on_delete=models.SET_NULL,
                            related_name='pictures')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.title + ' ' + self.time

    class Meta:
        db_table = 'picture'

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                             null=True, default='', on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)
    content = models.TextField(verbose_name='Content', null=True)
    likes = GenericRelation(Like)

    def __str__(self):
        return str(self.time)

    class Meta:
        db_table = 'comment'