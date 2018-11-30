# -*- coding: utf-8 -*-

from django.conf.urls import url

from categories import views

urlpatterns = [
    url(r'^(?P<category>[\w-]+)$', views.category, name='view-category'),
]