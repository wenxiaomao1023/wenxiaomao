# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Reply(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    content = models.TextField(null=True, blank=True)
    datetime = models.DateTimeField()
    replyId = models.IntegerField()