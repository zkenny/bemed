from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^', views.home, name='home'),
    url(r'^$', views.index, name='index'),
]
