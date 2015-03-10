from django.conf.urls import patterns, url
from cocktail import views


urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^cocktail/$',views.cocktail, name='cocktail'),
    url(r'^search/$',views.search, name='search'),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^base/$',views.base, name='base'),





                       )