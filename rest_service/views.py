"""
Definition of views.
"""
from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from django.template import RequestContext
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Story, Picture
from serializers import StorySerializer, PictureSerializer, UserSerializer

def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def stories(request):
	stories = Story.objects.all()
	serializer = StorySerializer(stories, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def pictures(request):
	pictures = Picture.objects.all()
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
	serializer = StorySerializer(story)

	return Response(serializer.data)

@api_view(['POST'])
def create_picture(request):
	if(not request.user):
		return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def create_story(request):
	if(not request.user):
		return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def create_comment(request):
	if(not request.user):
		return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def add_like(request):
	if(not request.user):
		return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def create_user(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

