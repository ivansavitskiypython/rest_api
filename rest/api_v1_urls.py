# coding=utf-8
"""
Urlconf module for API v1
"""
from django.conf.urls import include, url
from rest_framework import routers
from article.views.users import UsersViewSet

v1_api = routers.DefaultRouter()

v1_api.register('users', UsersViewSet, 'users-v1')

urlpatterns = [
    url('^', include(v1_api.urls)),
]
