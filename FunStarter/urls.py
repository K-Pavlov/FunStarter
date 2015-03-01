"""
Definition of urls for FunStarter.
"""

from datetime import datetime

from django.conf.urls import patterns, url, include
from django.contrib import admin

from rest_service.viewsets import RouteConfig

route_config = RouteConfig()
route_config.register_routes()

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(route_config.get_router().urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)