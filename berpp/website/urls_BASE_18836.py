from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^', views.home, name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.index, name='about'),
    url(r'^schedule/$', views.index, name='schedule'),
    url(r'^extracurriculars/$', views.index, name='extra'),
]
