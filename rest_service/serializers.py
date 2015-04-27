from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from models import Category, Story, Picture, Comment, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'stories', 'pictures')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'time', 'comment', 'story', 'picture')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'likes', 'content', 'time', 'story', 'picture')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )

class PictureSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Picture
        fields = ('title', 'likes', 'image', 'category', 'user', 'time', 'comments')

class StorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Story
        fields = ('title', 'likes', 'content', 'category', 'user', 'time', 'comments')
