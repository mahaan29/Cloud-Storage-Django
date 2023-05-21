"""Cloud_Storage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^adduser/$', views.adduser, name='adduser'),
    url(r'^checkuser/$', views.checkuser, name='checkuser'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^uploadpage/$', views.uploadpage, name='uploadpage'),
    url(r'^downloadpage/$', views.downloadpage, name='downloadpage'),

    url(r'^audioupload/$', views.audioupload, name='audioupload'),
    url(r'^photoupload/$', views.photoupload, name='photoupload'),
    url(r'^videoupload/$', views.videoupload, name='videoupload'),
    url(r'^fileupload/$', views.fileupload, name='fileupload'),

    url(r'^addaudio/$', views.addaudio, name='addaudio'),
    url(r'^addphoto/$', views.addphoto, name='addphoto'),
    url(r'^addvideo/$', views.addvideo, name='addvideo'),
    url(r'^addfile/$', views.addfile, name='addfile'),


    url(r'^audioview/$', views.audioview, name='audioview'),
    url(r'^photoview/$', views.photoview, name='photoview'),
    url(r'^videoview/$', views.videoview, name='videoview'),
    url(r'^fileview/$', views.fileview, name='fileview'),

    url(r'^audiodelete/(?P<audio_id>[0-9]+)/$', views.audiodelete , name='audiodelete'),
    url(r'^photodelete/(?P<photo_id>[0-9]+)/$', views.photodelete , name='photodelete'),
    url(r'^videodelete/(?P<video_id>[0-9]+)/$', views.videodelete , name='videodelete'),
    url(r'^filedelete/(?P<file_id>[0-9]+)/$', views.filedelete , name='filedelete'),

    url(r'^audiosearch/$', views.searchaudio , name='audiosearch'),
    url(r'^photosearch/$', views.searchphoto , name='photosearch'),
    url(r'^videosearch/$', views.searchvideo , name='videosearch'),
    url(r'^filesearch/$', views.searchfile , name='filesearch'),

    url(r'^audionotfound/$', views.audionotfound , name='audionotfound'),
    url(r'^photonotfound/$', views.photonotfound , name='photonotfound'),
    url(r'^videonotfound/$', views.videonotfound , name='videonotfound'),
    url(r'^filenotfound/$', views.filenotfound , name='filenotfound'),
]
