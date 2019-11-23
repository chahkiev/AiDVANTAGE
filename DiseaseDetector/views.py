# from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from DiseaseDetector.forms import UserLoginForm

from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View

from DiseaseDetector.models import *
from DiseaseDetector.forms import UserLoginForm

def main(request):
    return render(request, 'DiseaseDetector/base.html', )


def signin(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect(request.GET.get('next') if request.GET.get('next') != '' else '/')
	else:
		form = UserLoginForm()
		logout(request)
	return render(request, 'DiseaseDetector/signin.html', {'form': form})


def signout(request):
	if not request.user.is_authenticated:
		raise Http404
	logout(request)
	return redirect('/')