# -*- coding: utf-8 -*-
"""wenxiaomao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from article.views import article
from gallery.views import gallery, photo, getAlbumById, \
     album, getAlbums, getPhotos
from index.views import welcome, index, login, aboutme
from reply.views import reply, getReply, addReply


#from django.contrib import admin
urlpatterns = [
    #url(r'^admin/', admin.site.urls),

    url(r'^welcome/?$', welcome),
    
    url(r'^index/?$', index),
    
    url(r'^article/?$', article),
    
    #url(r'^music/?$', index),
    
    #相册
    #url(r'^gallery/\d+/?$', photo),
    url(r'^gallery/(?P<albumId>\d+)/(?P<photoId>\d+)/?$', photo),
    url(r'^gallery/(?P<albumId>\d+)/?$', album),
    url(r'^gallery/?', gallery),
    
    url(r'^getAlbums/(?P<albumId>\d+)/?$', getAlbumById),
    url(r'^getAlbums/?$', getAlbums),
    url(r'^getPhotos', getPhotos),
    
#     url(r'^photo/?$', photo),
    
    #留言板
    url(r'^reply/?$', reply),
    url(r'^getReply$', getReply),
    url(r'^addReply', addReply),
    
    url(r'^login/?$', login),
    
    url(r'^aboutme/?$', aboutme),
     
    url(r'^', welcome),
]
