# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import viewsets
from serializers import (
    UserSerializer,
    ArticleSerializer,
    ArticleSaveSerializer,
)
from django.db.models import Count
import django_filters
from rest_framework.decorators import detail_route
from rest_framework.viewsets import mixins, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from article.models import Article


class UserFilter(django_filters.FilterSet):
    posts_number = django_filters.CharFilter(method='custom_filter')
    class Meta:
        model = User
        fields = [
            'username',
            'posts_number',
        ]

    def custom_filter(self, queryset, name, value):
        return queryset.annotate(
            num_articles=Count('articles')
        ).filter(num_articles__gte=value)


class ArticleFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(method='username_filter')
    class Meta:
        model = Article
        fields = [
            'username',
        ]

    def username_filter(self, queryset, name, value):
        return queryset.filter(
            user=User.objects.get(
                username=value
            )
        )


class UserViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_class = UserFilter

    def get_queryset(self):
        return super(UserViewSet, self).get_queryset()


class ArticleViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Article.objects.all().order_by('-published_time')
    serializer_class = ArticleSerializer
    filter_class = ArticleFilter

    def get_queryset(self):
        return super(ArticleViewSet, self).get_queryset()


class UserArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSaveSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        self.serializer_class = ArticleSerializer
        self.queryset = self.queryset.filter(
            user=self.request.user
        )
        return super(UserArticleViewSet, self).get_queryset()
