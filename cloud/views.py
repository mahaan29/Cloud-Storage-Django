from django.shortcuts import render, redirect, get_object_or_404
from .models import customer, audiodata, photodata, videodata, filedata
import os.path
import os
from django.conf import settings
from django.http import HttpResponse, Http404



# app_name = 'cloud'cloud
# Create your views here.

def register(request):
    return render(request, 'cloud/register.html', {})

def login(request):
    return render(request, 'cloud/login.html', {})

def homepage(request):
    name = request.session.get('name')
    return render(request, 'cloud/homepage.html',{"name":name})

def uploadpage(request):
    return render(request, 'cloud/uploadpage.html')

def downloadpage(request):
    name = request.session.get('name')
    return render(request, 'cloud/downloadpage.html',{"name":name})


def audioupload(request):
    return render(request, 'cloud/audioupload.html')

def photoupload(request):
    return render(request, 'cloud/photoupload.html')

def videoupload(request):
    return render(request, 'cloud/videoupload.html')

def fileupload(request):
    return render(request, 'cloud/fileupload.html')

def videosearch(request):
    return render(request, 'cloud/videosearch.html')

def audioview(request):
    a = audiodata.objects.all()
    return render(request, 'cloud/audioview.html', {"a":a})

def photoview(request):
    a = photodata.objects.all()
    return render(request, 'cloud/photoview.html', {"a":a})

def videoview(request):
    a = videodata.objects.all()
    return render(request, 'cloud/videoview.html', {"a":a})

def fileview(request):
    a = filedata.objects.all()
    return render(request, 'cloud/fileview.html', {"a":a})

def logout(request):
    del request.session['id']
    del request.session['name']
    return login(request)

def addaudio(request):
    a1 = request.POST['name']
    a2 = request.POST['description']
    a3 = request.FILES['browse']
    print(a1, a2, a3)
    extension = os.path.splitext(str(request.FILES['browse']))
    ext = ['.mp3', '.mp4', '.wav', '.ogg', '.aac']
    if extension in ext:
        print("Your data is saved.")
    else:
        print("Please upload file of suitable format.")
    tab = audiodata(name=a1, description=a2, browse=a3)
    tab.save()
    return redirect('../audioupload/')

def addphoto(request):
    p1 = request.POST['name']
    p2 = request.POST['description']
    p3 = request.FILES['browse']
    print(p1, p2, p3)
    extension = os.path.splitext(str(request.FILES['browse']))
    ext = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls', '.jpeg']
    if extension in ext:
        print("Your data is saved.")
    else:
        print("Please upload file of suitable format.")
    tab = photodata(name=p1, description=p2, browse=p3)
    tab.save()
    return redirect('../photoupload/')

def addvideo(request):
    v1 = request.POST['name']
    v2 = request.POST['description']
    v3 = request.FILES['browse']
    print(v1, v2, v3)
    extension = os.path.splitext(str(request.FILES['browse']))
    ext = ['.mpg', '.mpeg', '.avi', '.wmv']
    if extension in ext:
        print("Your data is saved.")
    else:
        print("Please upload file of suitable format.")
    tab = videodata(name=v1, description=v2, browse=v3)
    tab.save()
    return redirect('../videoupload/')

def addfile(request):
    f1 = request.POST['name']
    f2 = request.POST['description']
    f3 = request.FILES['browse']
    print(f1, f2, f3)
    extension = os.path.splitext(str(request.FILES['browse']))
    ext = ['.doc', '.docx', '.pdf', '.rtf', '.txt', '.wpd']
    if extension in ext:
        print("Your data is saved.")
    else:
        print("Please upload file of suitable format.")
    tab = filedata(name=f1, description=f2, browse=f3)
    tab.save()
    return redirect('../fileupload/')

def adduser(request):
    print(request.POST)
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    email_id = request.POST['email_id']
    user_name = request.POST['user_name']
    password = request.POST['password']
    re_password = request.POST['re_password']

    if(password==re_password):
         cus = customer(first_name=fname, last_name=lname, email_id=email_id, user_name=user_name, password=password)
         cus.save()
         return render(request, 'cloud/login.html', {})

    else:
        message="passwords do not match"

def checkuser(request):
    try:
        print("CHECK 1 DONE!")
        n1 = request.POST['user_name']
        n2 = request.POST['password']
        cus = customer.objects.get(user_name=n1, password=n2)
        request.session['id'] = cus.id
        request.session['name'] = cus.user_name
        print("CHECK 2 DONE!")
        return homepage(request)
    except Exception as e:
        print(e)
        return render(request, 'cloud/login.html', {'error':'Invalid username/password'})

def audiodelete(request, audio_id):
    a = audiodata.objects.filter(id=audio_id)
    c = audiodata.objects.filter(id=audio_id).values('browse')
    f = c[0].get('browse')
    _delete_file(f)
    a.delete()
    b = audiodata.objects.all()
    return render(request, 'cloud/audioview.html', {"a": b})

def photodelete(request, photo_id):
    a = photodata.objects.filter(id=photo_id)
    c = photodata.objects.filter(id=photo_id).values('browse')
    f = c[0].get('browse')
    _delete_file(f)
    a.delete()
    b = photodata.objects.all()
    return render(request, 'cloud/photoview.html', {"a": b})

def videodelete(request, video_id):
    a = videodata.objects.filter(id=video_id)
    c = videodata.objects.filter(id=video_id).values('browse')
    f = c[0].get('browse')
    _delete_file(f)
    a.delete()
    b = videodata.objects.all()
    return render(request, 'cloud/videoview.html', {"a": b})

def filedelete(request, file_id):
    a = filedata.objects.filter(id=file_id)
    c = filedata.objects.filter(id=file_id).values('browse')
    f = c[0].get('browse')
    _delete_file(f)
    a.delete()
    b = filedata.objects.all()
    return render(request, 'cloud/fileview.html', {"a": b})

def _delete_file(file_name):
    path = settings.MEDIA_ROOT
    os.remove(os.path.join(path, file_name))

def audionotfound(request):
    return render(request, 'cloud/videonotfound.html')

def photonotfound(request):
    return render(request, 'cloud/videonotfound.html')

def videonotfound(request):
    return render(request, 'cloud/videonotfound.html')

def filenotfound(request):
    return render(request, 'cloud/videonotfound.html')


def searchaudio(request):
    e = request.POST['audioname']
    if audiodata.objects.filter(name=e).exists():
        f = audiodata.objects.get(name=e)
        return render(request, 'cloud/audiosearch.html', {'f':f})
    else:
        return render(request, 'cloud/audionotfound.html')

def searchphoto(request):
    e = request.POST['photoname']
    if photodata.objects.filter(name=e).exists():
        f = photodata.objects.get(name=e)
        return render(request, 'cloud/photosearch.html', {'f':f})
    else:
        return render(request, 'cloud/photonotfound.html')

def searchvideo(request):
    e = request.POST['videoname']
    if videodata.objects.filter(name=e).exists():
        f = videodata.objects.get(name=e)
        return render(request, 'cloud/videosearch.html', {'f':f})
    else:
        return render(request, 'cloud/videonotfound.html')

def searchfile(request):
    e = request.POST['filename']
    if filedata.objects.filter(name=e).exists():
        f = filedata.objects.get(name=e)
        return render(request, 'cloud/filesearch.html', {'f':f})
    else:
        return render(request, 'cloud/filenotfound.html')













