from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
    pass

    class Meta:
        db_table = 'story'

class Picture(models.Model):
    
    class Meta:
        db_table = 'picture'

class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)

    class Meta:
        db_table = 'category'

class Comment(models.Model):

    class Meta:
        db_table = 'comment'

class Like(models.Model):
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                             null=True, default='', on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True, default='', verbose_name='Time')

    class Meta:
        db_table = 'like'