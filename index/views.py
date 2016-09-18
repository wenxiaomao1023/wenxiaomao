# -*- coding: utf-8 -*-
import json

from django.contrib.auth import authenticate
from django.contrib.auth.views import logout
from django.http.response import HttpResponse, Http404
from django.shortcuts import render
from django.template.context_processors import csrf
from django.utils.translation import ugettext
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

# Create your views here.
def ret(state,msg=''):
    if state:
        s="SUCCESS"
    else:
        s="FAILURE"
    m=""    
    if msg!="":    
        m=unicode(str(msg),"utf-8")
        m=ugettext(m)
    return json.dumps({'state':s,'msg':m})

def welcome(request):
    return render(request,"welcome.html")

def index(request):
    return render(request,"index.html",{'audioplayer':True})

def aboutme(request):
    return render(request,"aboutme.html")

def login(request):
    return render(request,"login.html")


def userChangePassword(request):
    if(request.method == "POST"):
        password_old = request.POST['password_old']
        password_new = request.POST['password_new']
        password_new_verify = request.POST['password-v']
#         current_pwd = request.user.password
        if not request.user.check_password(password_old):
            return HttpResponse(json.dumps({'Success': False, 'errorInfo': '输入的密码不正确!'}))
        elif len(password_new)<6:
            return HttpResponse(json.dumps({'Success': False, 'errorInfo': '新密码需要大于5位数!'}))
        elif not password_new_verify == password_new:
            return HttpResponse(json.dumps({'Success': False, 'errorInfo': '两次输入的密码不一致!'}))
        try:
            request.user.set_password(password_new)
            request.user.save()
        except Exception, e:
            return HttpResponse(json.dumps({'Success': False, 'errorInfo': '更新密码失败!'}))
        else:
            return HttpResponse(json.dumps({'Success': True}))
    raise Http404() 

@ensure_csrf_cookie
def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        data = {}
        if(request.GET.__contains__('next') and request.GET['next'] != ''):
            data.update({'next':request.GET['next']})
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            data.update({'INCORRECT': False})
            return HttpResponse(json.dumps(data))
        else:
            data.update({'INCORRECT': True})
            return HttpResponse(json.dumps(data))
    c = {}
    c.update(csrf(request))
    logout(request)
    return render(request,"login.html", c)

def userLogout(request):
    logout(request)
    return HttpResponse(json.dumps({'success':True}))

