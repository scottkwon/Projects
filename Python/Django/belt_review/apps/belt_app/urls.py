from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.dashboard, name='dashboard'),
    url(r'^books/add/$', views.add_page, name='add_page'),
    url(r'^books/create_book/$', views.create_book, name='create_book'),
    url(r'^books/(?P<id>\d+)/$', views.book_review, name='book_review'),
    url(r'^books/create_review/$', views.create_review, name='create_review'),
    url(r'^users/(?P<id>\d+)/$', views.user_page, name='user_page'),
    url(r'^logout/$', views.logout, name='logout'),
]
