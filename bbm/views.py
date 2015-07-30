from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	template = loader.get_template('bbm/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def members(request):
	template = loader.get_template('bbm/members.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def music(request):
	template = loader.get_template('bbm/music.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def photos(request):
	template = loader.get_template('bbm/photos.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def videos(request):
	template = loader.get_template('bbm/videos.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))