from datetime import datetime
import json
import os

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from article.models import ArticleCategory, Article
from index.views import ret
from wenxiaomao.settings import MEDIA_ROOT, ARTICLE_PATH


def getArticleCategory(request):
    items = ArticleCategory.objects.all()
    total = items.count()
    jsonword = []
    for item in items:
        data = {'categoryId':item.id,
              'categoryName':item.name}
        jsonword.append(data)
    return HttpResponse(json.dumps({'total':total, 'rows':jsonword}))

@login_required
def adminArticle(request, articleId=None):
    if articleId != None:
        article = Article.objects.get(id=articleId)
        jsn = {'method':'edit',
             'articleId':articleId,
             'title':article.title,
             'desc':article.desc,
             'content':article.content,
             'categoryId':article.categoryId_id,
             'datetime':article.datetime.strftime('%Y-%m-%d %H:%M')}
    else:
        jsn = {'method':'add'}
    return render(request, 'admin/article.html', {'data':json.dumps(jsn)})

def uploadarticle(request):
    method = request.POST['method']
    articleId = request.POST['articleId']
    dt = request.POST['datetime']
    title = request.POST['title']
    categoryId = int(request.POST['categoryId'])
    desc = request.POST['desc']
    content = request.POST['content']
    if method == 'add':
        a = Article(title=title, desc=desc, content=content, datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), categoryId_id=categoryId)
        a.save()
    elif method == 'edit':
        a = Article.objects.get(id=articleId)
        a.title = title
        a.desc = desc
        a.content = content
        a.categoryId_id = categoryId
        a.datetime = dt
        a.save()
    return HttpResponse(ret(True, 'Done'))

def uploadfile(request, prev):
    _file = request.FILES['filedata']  # .getlist('filedata')
    _type = _file.name.split('.')[1]
    _file.name = '%s%s.%s' % (prev, datetime.now().strftime('%Y%m%d%H%M%S'), _type)
    dt = datetime.now().strftime('%Y%m%d')
    _dir = '%s%s%s/' % (MEDIA_ROOT, ARTICLE_PATH, dt)
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    f_path = '%s%s' % (_dir, _file.name)
    with open(f_path, 'wb+') as info:
        for chunk in _file.chunks():
            info.write(chunk)
    return HttpResponse(json.dumps({'err':'', 'msg':'%s://%s/%s%s/%s' % (request.scheme, request.get_host(), ARTICLE_PATH, dt, _file.name)}))

@login_required
def uploadlink(request):
    return uploadfile(request, 'l')

@login_required
def uploadimg(request):
    return uploadfile(request, 'i')

@login_required
def uploadflash(request):
    return uploadfile(request, 'f')

@login_required
def uploadmedia(request):
    return uploadfile(request, 'm')

def articleById(request, articleId=None):
    return articleFilter(request, articleId=articleId)

def articleByCategoryId(request, categoryId=None, pageIndex=None):
    return articleFilter(request, pageIndex=pageIndex, categoryId=categoryId)
    
def articleFilter(request, pageIndex=None, categoryId=None, articleId=None):
    jsn = {}
    if articleId != None:
        jsn = getArticle(request, articleId=articleId)
    else:
        if categoryId != None:
            jsn = getArticle(request, pageIndex=pageIndex, categoryId=categoryId)
        elif pageIndex != None:
            jsn = getArticle(request, pageIndex=pageIndex)    
        else:
            jsn = getArticle(request, pageIndex=1)
    return render(request, 'article.html', {'articlecategory':True, 'data':jsn})

def getArticle(request, pageIndex=None, categoryId=None, articleId=None):
    is_article = False
    catId = 0
    if articleId != None:
        items = Article.objects.filter(id=articleId)
        is_article = True
        pindex = 0
        pmax = 0
    else:
        showMax = 10
        pageIndex = int(pageIndex)
        if categoryId != None:
            catId = categoryId
            items = Article.objects.filter(categoryId_id=categoryId)
            c = items.count()
            items = items.order_by('-datetime')[(pageIndex - 1) * showMax:pageIndex * showMax]
        else:
            items = Article.objects.all()
            c = items.count()
            items = items.order_by('-datetime')[(pageIndex - 1) * showMax:pageIndex * showMax]
        if c % showMax == 0:    
            pmax = c / showMax
        else:
            pmax = c / showMax + 1
        pindex = pageIndex
    total = items.count()
    jsonword = []
    for item in items:
        data = {'id':item.id,
              'title':item.title,
              'desc':item.desc,
              'content':item.content,
              'datetime':item.datetime.strftime('%Y-%m-%d %H:%M'),
              'categoryId':item.categoryId_id,
              'categoryName':ArticleCategory.objects.get(id=item.categoryId_id).name,
              'is_article':is_article,
              'readmore':(item.categoryId_id != 1)}
        jsonword.append(data)
    return json.dumps({'total':total, 'rows':jsonword, 'pageIndex':pindex, 'pageMax':pmax, 'categoryId':catId})
    
