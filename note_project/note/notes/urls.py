from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes.views import index_view

urlpatterns = patterns('',
	url(r'^$', index_view, name='index'),
)