# -*- coding: utf-8 -*-
import json

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import login, logout
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, \
    csrf_exempt

from article.models import Article, ArticleCategory
from gallery.models import Photo
from wenxiaomao.settings import GALLERY_PATH


def ret(state=True, msg='', data={}):
    if state:
        s = "SUCCESS"
    else:
        s = "FAILURE"
    msg = unicode(str(msg), "utf-8")
    m = ugettext(msg)
    return json.dumps({'state':s, 'msg':m, 'data':data})

def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    return render(request, 'index.html', {'audioplayer':True})

def aboutme(request):
    return render(request, 'aboutme.html')

def login_url(request):
    return render(request, 'login.html')

def register_url(request):
    return render(request, 'register.html')

def htmlEncode(str):
    s=''
    if len(str) == 0: 
        return "";
    s = str.replace('&', '&gt;')   
    s = s.replace('<', '&lt;');   
    s = s.replace('>', '&gt;');   
    #s = s.replace(' ', '&nbsp;');   
    #s = s.replace('\'', '&#39;');   
    #s = s.replace('\"', '&quot;');   
    s = s.replace(r'\n', '<br>');
    return s;   

def getRecentUpdate(request):
    pageIndex=int(request.GET['pageIndex'])
    items = Article.objects.all().order_by('-datetime')
    total = items.count()
    limit=10
    jsonword = []
    for item in items[pageIndex*limit:(pageIndex+1)*limit]: 
#     for item in items: 
        data = {'id':item.id,
              'title':item.title,
              'desc':item.desc,
              'datetime':item.datetime.strftime('%Y-%m-%d %H:%M'),
              'ym':item.datetime.strftime('%Y-%m'),
              'categoryId':item.categoryId_id,
              'categoryName':ArticleCategory.objects.get(id=item.categoryId_id).name,
              'readmore':(item.categoryId_id != 1)}
        jsonword.append(data)
#     return HttpResponse(json.dumps({'total':limit, 'rows':jsonword, 'loadmore':loadmore }))
    return HttpResponse(json.dumps({'total':total, 'rows':jsonword, 'loadmore':(pageIndex+1)*limit<total }))

@csrf_exempt
def adminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            url=request.POST['next'].split('next=')
            if len(url)>1 and url[1]!='':
                return HttpResponseRedirect(url[1],user)
            else:
                return HttpResponseRedirect("/index")
        else:
            return HttpResponse(ret(False,'invalid username or password'))
        
def adminRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            if User.objects.filter(username=username).count()>0:
                return HttpResponse(ret(False,'username exist'))
            user = User.objects.create_user(username, username, password)
            user.save()
            currentuser = authenticate(username=username, password=password)
            login(request, currentuser) 
        except Exception, e:
            return HttpResponse(ret(False,e))
        else:
            return HttpResponseRedirect("/index",currentuser)
    raise Http404()

@login_required
def adminLogout(request):
    logout(request)
    return HttpResponseRedirect("/index")

