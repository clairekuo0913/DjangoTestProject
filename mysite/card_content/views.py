from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Profile
from django.template.loader import get_template

#Create your views here.
def hello_world(request):
	return render(request, 'index.html', {
			'current_time': str(datetime.now()),
		})

def index(request):
	template = get_template('index.html')
	# post_list = Post.objects.all()
	profile = Profile.objects.get(title='Default')
	html = template.render({'profile': profile})
	return HttpResponse(html)

def happybirthday(request):
	template = get_template('single.html')
	html = template.render()
	return HttpResponse(html)