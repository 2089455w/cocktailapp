from django.conf.urls import patterns, url
from cocktail import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),)