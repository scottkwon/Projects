from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process/$', views.process, name='process'),
    url(r'^login/$', views.login, name='login'),
    url(r'^secrets/$', views.secrets, name='secrets'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^post/$', views.post, name='post'),
    url(r'^like/(?P<id>\d+)$', views.like, name='like'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^user$', views.user, name='user')
]
