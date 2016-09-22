import json

from django.http.response import HttpResponse
from django.shortcuts import render

from article.models import ArticleCategory, Article


def getArticleCategory(request):
    items=ArticleCategory.objects.all()
    total=items.count()
    jsonword=[]
    for item in items:
        data={"categoryId":item.id,
              "categoryName":item.name}
        jsonword.append(data)
    return HttpResponse(json.dumps({'total':total, 'rows':jsonword}))

def article(request,categoryId=None,articleId=None):
    jsn={}
    if articleId!=None:
        jsn=getArticleById(request,categoryId,articleId)
    else:
        if categoryId!=None:
            jsn=getArticleByCategoryId(request,categoryId)
        else:
            jsn=getArticle(request)
    return render(request,"article.html",{"articlecategory":True,"data":jsn})

def getArticle(request,categoryId=None,articleId=None):
    is_article=False
    if articleId!=None:
        items=Article.objects.filter(id=articleId)
        is_article=True
    else:
        if categoryId!=None:
            items=Article.objects.filter(categoryId_id=categoryId)
        else:
            items=Article.objects.all()
    total=items.count()
    jsonword=[]
    for item in items:
        data={"id":item.id,
              "title":item.title,
              "desc":item.desc,
              "content":item.content,
              "datetime":item.datetime.strftime("%Y-%m-%d %H:%M"),
              "categoryId":item.categoryId_id,
              "categoryName":ArticleCategory.objects.get(id=item.categoryId_id).name,
              "is_article":is_article}
        jsonword.append(data)
    return json.dumps({'total':total, 'rows':jsonword})
    
def getArticleByCategoryId(request,categoryId):
    return getArticle(request,categoryId)

def getArticleById(request,categoryId,articleId):
    return getArticle(request,categoryId,articleId)
