# from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from DiseaseDetector.forms import UserLoginForm

from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.http.request import HttpRequest

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

def profile(request, username):
	user = User.objects.by_username(username)
	if user is not None:
		return render(request, 'DiseaseDetector/profile.html', {'profile': user})
	else:
		raise Http404


def anketa(request):
    return render(request, 'DiseaseDetector/anketa.html', )


def survey_questionnaire(request: HttpRequest) -> HttpResponse:
    survey_json = {
        "locale": "ru",
        "loadingHtml": "Загрузка",
        "pages": [
            {
                "name": "page1",
                "elements": [
                    {
                        "type": "text",
                        "name": "FIO",
                        "title": "ФИО",
                        "isRequired": True,
                        "requiredErrorText": "Пожалуйста заполните поле"
                    },
                    {
                        "type": "dropdown",
                        "name": "Doctor",
                        "title": "Выберите врача",
                        "isRequired": True,
                        "requiredErrorText": "Пожалуйста заполните поле",
                        "commentText": "Выберите врача",
                        "choices": [
                            {
                                "value": "1",
                                "text": "Врач 1"
                            },
                            {
                                "value": "2",
                                "text": "Врач 2"
                            },
                            {
                                "value": "3",
                                "text": "Врач 3"
                            }
                        ],
                        "otherText": "Выберите врача",
                        "optionsCaption": "Выберите врача",
                        "showOptionsCaption": False
                    },
                    {
                        "type": "dropdown",
                        "name": "Time",
                        "title": "Время приема",
                        "choices": [
                            {
                                "value": "1",
                                "text": "10:00"
                            },
                            {
                                "value": "2",
                                "text": "10:10"
                            },
                            {
                                "value": "3",
                                "text": "10:20"
                            }
                        ],
                        "showOptionsCaption": False
                    },
                    {
                        "type": "checkbox",
                        "name": "Personal info",
                        "title": "Согласие на обработку персональных данных",
                        "isRequired": True,
                        "requiredErrorText": "Пожалуйста заполните поле",
                        "choices": [
                            {
                                "value": "1",
                                "text": "Даю согласие на обработку персональных данных"
                            }
                        ]
                    }
                ],
                "title": "Личная информация",
                "navigationButtonsVisibility": "show"
            },
            {
                "name": "page2",
                "elements": [
                    {
                        "type": "radiogroup",
                        "name": "question1",
                        "title": "Вопрос 1",
                        "isRequired": True,
                        "choices": [
                            {
                                "value": "item1",
                                "text": "Ответ 1"
                            },
                            {
                                "value": "item2",
                                "text": "Ответ 2"
                            },
                            {
                                "value": "item3",
                                "text": "Ответ 3"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "page3",
                "elements": [
                    {
                        "type": "radiogroup",
                        "name": "question2",
                        "title": "Вопрос 2",
                        "isRequired": True,
                        "choices": [
                            {
                                "value": "item1",
                                "text": "Да"
                            },
                            {
                                "value": "item2",
                                "text": "Нет"
                            }
                        ]
                    }
                ]
            }
        ],
        "showQuestionNumbers": "off",
        "showProgressBar": "top",
        "goNextPageAutomatic": True,
        "startSurveyText": "Начать анкету",
        "pagePrevText": "Вернуться",
        "pageNextText": "Далее",
        "completeText": "Завершить"
    }

    return JsonResponse(survey_json)
