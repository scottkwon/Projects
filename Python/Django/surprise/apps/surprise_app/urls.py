from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/$', views.process),
    url(r'^surprises/$', views.surprises),
    url(r'^reset/$', views.reset)
]
