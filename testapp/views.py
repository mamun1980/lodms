from django.shortcuts import render
from django.conf import settings
from django.utils.safestring import mark_safe
import os
# Create your views here.
from .models import *



def testapp_home(request):
	rooms = Room.objects.all()
	media_path = settings.MEDIA_ROOT + "/" + mark_safe('904-2016-2017')
	file_list = []
	for files in os.walk(media_path):
		for file in files:
			file_list.append(file)

	return render(request, 'home.html', 
		{'room': rooms, 'media_path': media_path, 'file_list': file_list})