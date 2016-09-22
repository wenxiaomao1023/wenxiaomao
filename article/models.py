from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    datetime = models.DateTimeField()
    categoryId = models.ForeignKey(ArticleCategory)
