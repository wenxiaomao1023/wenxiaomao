import json

from django.http.response import HttpResponse
from django.shortcuts import render

from gallery.models import Album, Photo

GALLERY_PATH="/static/gallery/"
# Create your views here.
def gallery(request):
    return render(request,"gallery.html")

def getAlbums(request,albumId=None):
    if albumId!=None:
        items=Album.objects.filter(id=albumId)
    else:
        items=Album.objects.all()
    total=items.count()
    jsonword=[]
    for item in items: 
        data = []
        data = {'id':item.id,
                'name':item.name, 
                'cover':'http://%s%s%s'%(request.get_host(),GALLERY_PATH,item.cover),
                'datetime':item.datetime.strftime("%Y-%m-%d %H:%M:%S"),
                'total':Photo.objects.filter(albumId_id=item.id).count()}
        jsonword.append(data)
    return HttpResponse(json.dumps({'total':total, 'rows':jsonword}))

def getAlbumById(request,albumId):
    return getAlbums(request,albumId)

def photo(request,albumId,photoId):
    context={"albumId":albumId}
    return render(request,"photo.html",context)

def album(request,albumId):
    context={"albumId":albumId}
    return render(request,"album.html",context)

def getPhotos(request):
    albumId=request.GET["albumId"]
    items=Photo.objects.filter(albumId_id=albumId)
    total=items.count()
    jsonword=[]
    for item in items: 
        data = []
        data = {'id':item.id,
                'desc':item.desc, 
                'path':'http://%s%s%s'%(request.get_host(),GALLERY_PATH,item.path),
                'datetime':item.datetime.strftime("%Y-%m-%d %H:%M:%S"),
                'albumId':item.albumId_id}
        jsonword.append(data)
    return HttpResponse(json.dumps({'total':total, 'rows':jsonword}))

