# from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from DiseaseDetector.forms import UserLoginForm

from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import auth

from DiseaseDetector.forms import UserLoginForm, UserRegistrationForm
from DiseaseDetector.models import *
from .domain.survey import surveyjs_io_json, OncologyAlertnessQuestionnaire


def main(request):
    return redirect('signin')

def signup(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.set_password(form.cleaned_data['password'])
			user.save()
			login(request, user)
			return redirect('/')
	else:
		form = UserRegistrationForm()
		logout(request)
	return render(request, 'DiseaseDetector/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/survey')

    if request.method == 'GET':
        if auth.get_user(request).is_anonymous:
            form = UserLoginForm()
            return render(request, 'DiseaseDetector/signin.html', {'form': form})
        else:
            return redirect('/survey')
    


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def profile(request, username):
    user = User.objects.by_username(username)
    if user is not None:
        return render(request, 'DiseaseDetector/profile.html', {'profile': user})
    else:
        raise Http404


def survey(request):
    #if auth.get_user(request).is_anonymous:
    #    return redirect('/signin')
    #else:
        return render(request, 'DiseaseDetector/survey.html', )

def survey_questionnaire(request: HttpRequest) -> HttpResponse:
    return JsonResponse(surveyjs_io_json, safe=False)


def survey_response(request: HttpRequest) -> HttpResponse:
    result = OncologyAlertnessQuestionnaire.from_json(request.body)
    # TODO: create database for answer
    # TODO: save as json to database
