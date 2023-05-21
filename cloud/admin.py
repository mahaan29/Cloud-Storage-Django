from django.contrib import admin
from .models import customer, audiodata, photodata, videodata, filedata

# Register your models here.

admin.site.register(customer)
admin.site.register(audiodata)
admin.site.register(photodata)
admin.site.register(videodata)
admin.site.register(filedata)