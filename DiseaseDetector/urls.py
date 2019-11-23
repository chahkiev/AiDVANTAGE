from django.conf.urls import url

from DiseaseDetector.views import *

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^survey_questionnaire\.json$', survey_questionnaire, name='survey_questionnaire.json'),
]
