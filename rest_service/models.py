from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import datetime

def only_one_liked(list):
    true_found = False
    for v in list:
        if v:
            # a True was found!
            if true_found:
                # found too many True's
                return False 
            else:
                # found the first True
                true_found = True
    # found zero or one True value
    return true_found

class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'category'

class Story(models.Model):
    title = models.CharField(verbose_name='Title', max_length='200', null=True)
    content = models.TextField(verbose_name='Content', null=True)
    category = models.ForeignKey(Category, verbose_name='Category', blank=True,
                                null=True, default=None, on_delete=models.SET_NULL,
                                related_name='stories')
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                            null=True, default=None, on_delete=models.SET_NULL,
                            related_name='stories')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)

    def __str__(self):
        return str(self.title) + ' ' + str(self.time)
     
    class Meta:
        db_table = 'story'

class Picture(models.Model):
    title = models.CharField(verbose_name='Title', max_length='200', null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Image', null=True)
    category = models.ForeignKey(Category, verbose_name='Category', blank=True,
                                null=True, default=None, on_delete=models.SET_NULL,
                                related_name='pictures')
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                            null=True, default=None, on_delete=models.SET_NULL,
                            related_name='pictures')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)

    def __str__(self):
        return str(self.title) + ' ' + str(self.time)

    class Meta:
        db_table = 'picture'

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                             null=True, default=None, on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)
    content = models.TextField(verbose_name='Content', null=True)
    story = models.ForeignKey(Story, verbose_name='Story', blank=True,
                            null=True, default=None, on_delete=models.SET_NULL,
                            related_name='comments')
    picture = models.ForeignKey(Picture, verbose_name='Picture', blank=True,
                            null=True, default=None, on_delete=models.SET_NULL,
                            related_name='comments')

    def clean(self):
        if(not only_one_liked([self.story, self.picture])):
            raise ValidationError('One like should be for one entity')

    def save(self, *args, **kwargs):
        self.clean()

        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.time)

    class Meta:
        db_table = 'comment'

class Like(models.Model):
    user = models.ForeignKey(User, verbose_name='User', blank=True,
                             null=True, default='', on_delete=models.SET_NULL,
                             related_name='likes')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time', default=datetime.now)
    story = models.ForeignKey(Story, verbose_name='Story', blank=True,
                            null=True, default=None, on_delete=models.SET_NULL,
                            related_name='likes')
    picture = models.ForeignKey(Picture, verbose_name='Picture', blank=True,
                            null=True, default=None, on_delete=models.SET_NULL,
                            related_name='likes')
    comment = models.ForeignKey(Comment, verbose_name='Comment', blank=True,
                                null=True, default=None, on_delete=models.SET_NULL,
                                related_name='likes')

    def clean(self):
        if(not only_one_liked([self.comment, self.story, self.picture])):
            raise ValidationError('One like should be for one entity')

    def save(self, *args, **kwargs):
        self.clean()

        super(Like, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user) + ' ' + str(self.time) 

    class Meta:
        db_table = 'like'