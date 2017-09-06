# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    user = models.ForeignKey(
        User, verbose_name='Автор', related_name='articles'
    )
    published_time = models.DateTimeField(
        'Дата создания', auto_now_add=True, db_index=True, editable=False,
    )
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __unicode__(self):
        return u'%s - %s' % (self.title, self.user)
