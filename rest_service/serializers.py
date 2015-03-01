from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from models import Category, Story, Picture, Comment, Like

class LikedObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if(isinstance(value, Comment)):
            print 'here'
            serializer = CommentSerializer(value)
        elif(isinstance(value, Picture)):
            serializer = PictureSerializer(value)
        elif(isinstance(value, Story)):
            serializer = StorySerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'stories', 'pictures')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'stories', 'pictures')

### Change to like count only ??? ###
class StorySerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Story
        fields = ('title', 'likes', 'content', 'category', 'user', 'time')

class PictureSerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Picture
        fields = ('title', 'likes', 'image', 'category', 'user', 'time')

class CommentSerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'likes', 'content', 'time')
        
class LikeSerializer(serializers.ModelSerializer):
    content_object = LikedObjectRelatedField(read_only=True)
    content_type = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = ('user', 'time', 'content_type', 'content_object')