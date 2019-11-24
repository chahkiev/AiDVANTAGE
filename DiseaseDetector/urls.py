from django.conf.urls import url

from DiseaseDetector.views import *

urlpatterns = [
    url(r'^$', signin, name='signin'),
    url(r'^signout/$', signout, name='signout'),

    url(r'^survey/$', survey, name='survey'),
    url(r'^survey_questionnaire\.json$', survey_questionnaire, name='survey_questionnaire.json'),

    url(r'^user/(?P<username>[a-zA-Zа-яА-Я _\-.0-9]+?)$', profile, name='profile'),
]
