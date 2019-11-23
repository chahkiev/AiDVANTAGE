from django.conf.urls import url
from django.urls import path
from DiseaseDetector.views import *

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^signin/$', signin, name='signin'),
    url(r'^signout/$', signout, name='signout'),
]