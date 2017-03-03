import json

from django.http.response import HttpResponse
from django.shortcuts import render

from gallery.models import Album, Photo
from wenxiaomao.settings import GALLERY_PATH

PAGE_SHOW_IMG_NUM=4

def gallery(request):
    return render(request, 'gallery.html', {'is_gallery':True})

def getAlbums(request, albumId=None):
    if albumId != None:
        items = Album.objects.filter(id=albumId)
    else:
        items = Album.objects.all()
    total = items.count()
    jsonword = []
    for item in items: 
        data = {'id':item.id,
                'name':item.name,
                'cover':'%s://%s/%s%s' % (request.scheme, request.get_host(), GALLERY_PATH, item.cover),
                'datetime':item.datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'total':Photo.objects.filter(albumId_id=item.id).count()}
        jsonword.append(data)
    return HttpResponse(json.dumps({'total':total, 'rows':jsonword}))

def getAlbumById(request, albumId):
    return getAlbums(request, albumId)

def album(request, albumId):
    context = {'albumId':albumId,
             'is_album':True,
             'PAGE_SHOW_IMG_NUM':PAGE_SHOW_IMG_NUM}
    return render(request, 'album.html', context)

def getPhotos(request):
    albumId = request.GET['albumId']
    pageIndex = int(request.GET['pageIndex'])
    items = Photo.objects.filter(albumId_id=albumId)
    # total=items.count()
    limit = PAGE_SHOW_IMG_NUM
    loadmore = False
    if (pageIndex + 1) * limit < items.count():
        loadmore = True
    jsonword = []
    for item in items[pageIndex * limit:(pageIndex + 1) * limit]: 
        data = {'id':item.id,
                'desc':item.desc,
                'path':'%s://%s/%s%s' % (request.scheme, request.get_host(), GALLERY_PATH, item.path),
                'datetime':item.datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'albumId':item.albumId_id}
        jsonword.append(data)
    return HttpResponse(json.dumps({'total':limit, 'rows':jsonword, 'loadmore':loadmore }))

