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
    # TODO: доделать регистрацию - как определять, какой пользователь прислал ответ?
    # TODO: fix error
    # Forbidden (CSRF token missing or incorrect.): /survey_response/
    # [24/Nov/2019 20:54:23] "POST /survey_response/ HTTP/1.1" 403 2513

    url(r'^survey_response/$', survey_response, name='survey_response'),

    # возвращает страницу с данными пользователя
    url(r'^user/(?P<username>[a-zA-Zа-яА-Я _\-.0-9]+?)$', profile, name='profile'),
]
