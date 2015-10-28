from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import (
	check_password, is_password_usable, make_password,
)

# from .forms import SignupForm


from .models import MyUser

def base(request):
	template = loader.get_template('bbm/base.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

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

def login(request):
	# error = "Your entered details seems invalid , Please try again !"
	# message = "Welcome back ! Login and Discuss with Your Congolese's Brothers"
	
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username , password=password)

		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('music.html')
		else:
			return HttpResponseRedirect('login.html')
	else:

		template = loader.get_template('bbm/login.html')
		context = RequestContext(request, {
			# 'message':message,
			# 'error':error
			})

		return HttpResponse(template.render(context))

def loggedin(request):
	template = loader.get_template('loggedin.html')
	context = RequestContext(request, {})

	return HttpResponse(template.render(context))

# def loginf(request):
# 	template = loader.get_template('loginf.html')
# 	context = RequestContext(request, {})

# 	return HttpResponse(template.render(context))

def register(request):
	# subtitle = 'Please Register !'
	# # location_list = Location.objects.all()
	# country_name = [liste.country for liste in location_list]
	# number_list = MatriculeNo.objects.all()
	# unique_number = [number.No for number in number_list]
	# message = 'Passwords does not match'

	if request.method == 'POST':
		username = request.POST.get('username', '')
		lastname = request.POST.get('lastname', '')
		firstname = request.POST.get('firstname', '')
		password1 = request.POST.get('password1', '')
		password2 = request.POST.get('password2', '')
		email = request.POST.get('email', '')
		# matricule = [request.POST.get('matricule')]

		# if len(matricule) == 0:
		# 	error = "The matricule your entered is not valid"
		# else:
		# 	error = "valid"
		if password1 != password2:
			# raise ValueError('Passwords does not match')
			# return HttpResponse(template.render(context))
			return HttpResponseRedirect('register.html')
		else:
			# password.set_password(request.POST.get['password2', ''])

			user = MyUser.objects.create(
			username = username,
			password = make_password(password2),
				first_name = firstname,
				last_name = lastname,
				email = email,
				# MatriculeNo = matricule
				# location = country
			  )

			if user is not None:
				return HttpResponseRedirect('login.html')
			else:
				return HttpResponseRedirect('register.html')

	# else:
	# 	return HttpResponseRedirect('/')
		

	template = loader.get_template('bbm/register.html')
	context = RequestContext(request, {
		# 'message': message,
		# 'subtitle': subtitle,
		# 'location_list': location_list,
		# 'country_name' : country_name,
		# 'number_list': number_list,
		# 'unique_number': json.dumps(unique_number),
		# 'error' : error
		# 'form' : SignupForm()
	})


	return HttpResponse(template.render(context))

def logout(request):
	# message = "You have successfully logged out !"
	auth.logout(request)
	template = loader.get_template('bbm/index.html')
	context = RequestContext(request, {
		 # 'message': message
		})
	return HttpResponse(template.render(context))
