from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blog/$', views.blog),
    url(r'^about_me/$', views.about_me),
    url(r'^projects/$', views.projects),
]
