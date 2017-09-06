from django.contrib.auth.models import User, Group
from models import Article
from collections import OrderedDict
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('_get_username')
    class Meta:
        model = Article
        fields = (
            'username',
            'id',
            'title',
            'body',
            'published_time'
        )
    def _get_username(self, article):
        """
        Returns username of author
        """
        return article.user.username


class ArticleSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'body',
            'published_time'
        )


class UserSerializer(serializers.ModelSerializer):
    number_articles = serializers.SerializerMethodField('_get_number_articles')
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'date_joined',
            'number_articles',
        )

    def _get_number_articles(self, user):
        """
        Returns number of articles
        """
        return len(user.articles.all())
