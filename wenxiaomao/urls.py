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

from article.views import getArticleCategory, adminArticle, \
    uploadlink, uploadimg, uploadflash, \
    uploadmedia, uploadarticle, articleById, articleByCategoryId
from gallery.views import gallery, getAlbumById, \
     album, getAlbums, getPhotos, adminGallery
from index.views import welcome, index, login, aboutme, getRecentUpdate, \
    adminLogin, adminRegister, adminLogout, login_url, register_url
from reply.views import reply, getReply, addReply


#from django.contrib import admin
urlpatterns = [
    ##############################################################################
    #首页
    url(r'^index/?$', index),
    url(r'^getRecentUpdate', getRecentUpdate),
    ##############################################################################
    #文章
    url(r'^admin/article/?$', adminArticle),
    url(r'^admin/article/a(?P<articleId>\d+)/?$', adminArticle),
    url(r'^uploadarticle', uploadarticle),
    url(r'^uploadlink', uploadlink),
    url(r'^uploadimg', uploadimg),
    url(r'^uploadflash', uploadflash),
    url(r'^uploadmedia', uploadmedia),
    url(r'^article/a(?P<articleId>\d+)/?$', articleById),
    url(r'^article/(?P<categoryId>\d+)/(?P<pageIndex>\d+)/?$', articleByCategoryId),
    url(r'^article/(?P<pageIndex>\d+)/?$', articleByCategoryId),
    url(r'^article/?$', articleByCategoryId),
    url(r'^getArticleCategory', getArticleCategory),
    ##############################################################################
    #相册
    url(r'^admin/gallery/?$', adminGallery),
    url(r'^admin/gallery/a(?P<albumId>\d+)/?$', adminGallery),
    url(r'^gallery/(?P<albumId>\d+)/?$', album),
    url(r'^gallery/?', gallery),
    url(r'^getAlbums/(?P<albumId>\d+)/?$', getAlbumById),
    url(r'^getAlbums/?$', getAlbums),
    url(r'^getPhotos', getPhotos),
    ##############################################################################
    #关于我
    url(r'^aboutme/?$', aboutme),
    ##############################################################################
    #留言板
    url(r'^reply/?$', reply),
    url(r'^getReply$', getReply),
    url(r'^addReply', addReply),
    ##############################################################################
    #url(r'^admin/', admin.site.urls),
    url(r'^login/?$', login_url),
    #url(r'^register/?$', register_url),
    url(r'^adminLogin', adminLogin),
    url(r'^adminRegister', adminRegister),
    url(r'^logout', adminLogout),
    url(r'^welcome/?$', welcome),
    url(r'^', index),
]
