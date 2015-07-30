from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^videos', views.videos, name='videos'),
	url(r'^photos', views.photos, name='photos'),
	url(r'^music', views.music, name='music'),
	url(r'^members', views.members, name='members'),
	url(r'^$', views.index, name='index'),
	]