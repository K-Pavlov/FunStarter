from django.contrib.auth.models import User
from rest_framework import routers, viewsets

from serializers import UserSerializer, CategorySerializer, StorySerializer, PictureSerializer, CommentSerializer, LikeSerializer
from models import Category, Story, Picture, Comment, Like

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class RouteConfig:
    pass
#    def __init__(self):
#        self.router = routers.DefaultRouter()
#
#    def register_routes(self):
#        self.router.register(r'users', UserViewSet)
#        self.router.register(r'categories', CategoryViewSet)
#        self.router.register(r'stories', StoryViewSet)
#        self.router.register(r'pictures', PictureViewSet)
#        self.router.register(r'comments', CommentViewSet)
#        self.router.register(r'likes', LikeViewSet)
#
#    def get_router(self): 
#        return self.router