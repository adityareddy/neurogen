from django.conf.urls import patterns, url

from nemo import views

urlpatterns = patterns('',
    url(r'^$', views.search, name='search'),
)