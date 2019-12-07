from django.conf.urls import url

from DiseaseDetector.views import *

urlpatterns = [
    # Главная .html странаца с регистрацией.
    url(r'^$', main, name='main'),

    url(r'^signin/$', signin, name='signin'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^signout/$', signout, name='signout'),

    # .html страница с опросом
    url(r'^survey/$', survey, name='survey'),

    # возвращает .json, который определяет анкету
    url(r'^survey_questionnaire\.json$', survey_questionnaire, name='survey_questionnaire.json'),

    # Получает ответ на анкету
    url(r'^survey_response/$', csrf_exempt(survey_response), name='survey_response'),

    # возвращает страницу с данными пользователя
    url(r'^user/(?P<username>[a-zA-Zа-яА-Я _\-.0-9]+?)$', profile, name='profile'),

    # отрисовывает страницу с результатами опросов
    url(r'^view_results/$', view_results, name='view_results'),
]
