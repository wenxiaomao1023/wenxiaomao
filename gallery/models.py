from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50)
    cover = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    
class Photo(models.Model):
    desc = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    albumId = models.ForeignKey(Album)