from django.conf.urls import url
from django.urls import path
from DiseaseDetector.views import *

urlpatterns = [
    url(r'^$', main, name='main'),
]