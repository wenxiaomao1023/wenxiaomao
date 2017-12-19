# -*- coding: utf-8 -*-
from datetime import datetime
import json

from django.http.response import HttpResponse
from django.shortcuts import render

from index.views import ret, htmlEncode
from reply.models import Reply


def reply(request):
    return render(request, 'reply.html')

def getReply(request):
    if(request.method == 'POST'):
        items = Reply.objects.all().filter(replyId=0)
        if(request.POST.__contains__('page')):
            page = int(request.POST['page'])
        else:
            page = 1
        jsonword = []
        total = items.count()
        showMax = 5
        for item in items.order_by('-datetime')[(page - 1) * showMax:page * showMax]: 
            data = []
            data = {'id':item.id,
                    'content':item.content,
                    'username':item.username,
                    'email':item.email,
                    'datetime':item.datetime.strftime('%Y-%m-%d %H:%M:%S'),
                    'reply_id':item.replyId,
                    'indent':0}
            jsonword.append(data)
            for i in queryAllReplyByRoot(item.id, 1):
                jsonword.append(i)
        return HttpResponse(json.dumps({'total':total, 'rows':jsonword}))

def addReply(request):
    if request.method == 'POST':
        content = htmlEncode(request.POST['content'])
        username = htmlEncode(request.POST['username'])
        email = htmlEncode(request.POST['email'])
        replyId = int(request.POST['replyId'])
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if username == '':
            jsn = ret(False, '请填写昵称')
        elif content == '':
            jsn = ret(False, '请填写留言内容')
        else:        
            reply = Reply(username=username, email=email, content=content, datetime=date_time, replyId=replyId)        
            reply.save()
            jsn = ret(True, '成功')
        return HttpResponse(jsn)

# 通过Id号查询到所有以此Id为根的回复
def queryAllReplyByRoot(rId, indent):
    lst = []
    items = Reply.objects.all().filter(replyId=rId)
    for item in items: 
        data = []
        data = {'id':item.id,
                'content':item.content,
                'username':item.username,
                'email':item.email,
                'datetime':item.datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'reply_id':item.replyId,
                'indent':indent}
        lst.append(data)
        for i in queryAllReplyByRoot(item.id, indent + 1):
            lst.append(i)
    return lst

