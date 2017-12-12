# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import Permission, User
from django import forms



@python_2_unicode_compatible
class News(models.Model):
    news_title = models.CharField(max_length = 200)
    news_body = models.TextField()
    news_author = models.CharField(max_length = 200)
    news_publisher = models.ForeignKey('auth.User', related_name='news_list', on_delete = models.CASCADE)
    news_date = models.DateField('date published')

    def __str__(self):
        return self.news_title
