"""
Definition of urls for FunStarter.
"""

from datetime import datetime

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken import views

from rest_service.viewsets import RouteConfig
from rest_service.views import index

route_config = RouteConfig()
route_config.register_routes()

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(route_config.get_router().urls)),
    url(r'^client', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/stories', 'rest_service.views.stories'),
    url(r'^api/pictures', 'rest_service.views.pictures'),
    url(r'^api/story', 'rest_service.views.story'),
    url(r'^api/picture', 'rest_service.views.picture'),
    url(r'^api/create-story', 'rest_service.views.create_story'),
    url(r'^api/create-picture', 'rest_service.views.create_picture'),
    url(r'^api/register-user', 'rest_service.views.register_user'),    
    url(r'^api/token-auth/', views.obtain_auth_token)
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)