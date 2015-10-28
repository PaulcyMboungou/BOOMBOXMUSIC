from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^logout', views.logout, name='logout'),
	url(r'^register', views.register, name='register'),
	url(r'^loggedin', views.loggedin, name='loggedin'),
	url(r'^login', views.login, name='login'),
	url(r'^base', views.base, name='base'),
	url(r'^videos', views.videos, name='videos'),
	url(r'^photos', views.photos, name='photos'),
	url(r'^music', views.music, name='music'),
	url(r'^members', views.members, name='members'),
	url(r'^$', views.index, name='index'),
	]