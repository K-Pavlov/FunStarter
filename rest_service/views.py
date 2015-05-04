"""
Definition of views.
"""
from datetime import datetime

from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpRequest
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Story, Picture, Comment
from serializers import StorySerializer, PictureSerializer,\
						UserSerializer, PictureCommentsSerializer, \
						StoryCommentSerializer, CommentSerializer

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def index(request):
	return render(request, 'index.html')

@api_view(['GET'])
def stories(request):
	stories = Story.objects.all().order_by('-time')
	serializer = StorySerializer(stories, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def pictures(request):
	pictures = Picture.objects.all().order_by('-time')
	serializer = PictureSerializer(pictures, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def picture(request, id):
	picture = Picture.objects.get(pk=id)
	serializer = PictureSerializer(picture)

	return Response(serializer.data)

@api_view(['GET'])
def story(request, id):
	story = Story.objects.get(pk=id)
	serializer = StoryCommentSerializer(story)
	print serializer.data
	return Response(serializer.data)

@api_view(['POST'])
def create_picture(request):
<<<<<<< HEAD
	token = getToken(request.META)
	user = getUser(token)

	if(not user):
=======
	if(not request.user) :
>>>>>>> 7592dd499cd8f0f44efd82cfea882d21963161eb
		return Response(status=status.HTTP_403_FORBIDDEN)

	serialized = PictureSerializer(data=request.DATA, files=request.FILES)

	if(serialized.is_valid):
		picture = Picture()
		picture.title = serialized.initial_data['title']
		picture.image = serialized.initial_data['image']
		picture.save()

		return Response(status=status.HTTP_201_CREATED)
	else:
		return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_story(request):
	token = getToken(request.META)
	user = getUser(token)

	if(not user):
		return Response(status=status.HTTP_403_FORBIDDEN)

	serialized = StorySerializer(data=request.DATA)

	if(serialized.is_valid):
		story = Story()
		story.title = serialized.initial_data['title']
		story.content = serialized.initial_data['content']
		story.save()

		return Response(status=status.HTTP_201_CREATED)
	else:
		return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_comment(request):
	token = getToken(request.META)
	user = getUser(token)

	if(not user):
		return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def add_like(request):
	token = getToken(request.META)
	user = getUser(token)

	if(not user):
		return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def register_user(request):
	serialized = UserSerializer(data=request.DATA)
	if serialized.is_valid():
	    User.objects.create_user(
	        serialized.initial_data['username'],
	        serialized.initial_data['email'],
	        serialized.initial_data['password']
	    )
	    return Response(status=status.HTTP_201_CREATED)
	else:
	    return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_comment(request, data_type, id):
	token = getToken(request.META)
	user = getUser(token)

	serialized = CommentSerializer(data=request.DATA)


	if(serialized.is_valid):
		comment = Comment()
		comment.content = serialized.initial_data['content']
		if(user):
			comment.user = user

		if(data_type == 'stories'):
			comment.story = Story.objects.get(pk=id)
		elif(data_type == 'pictures'):
			comment.picture = Picture.objects.get(pk=id)

		comment.save()

		serialized = CommentSerializer(comment)
		return Response(serialized.data, status=status.HTTP_201_CREATED)
	else:
	    return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


def getUser(token):
	try:
		return Token.objects.get(key=token).user
	except Token.DoesNotExist:
		return False

def getToken(request_meta):
	token = request_meta['HTTP_AUTHORIZATION'].split(' ')[1]

	return token
