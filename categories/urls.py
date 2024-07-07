# -*- coding: utf-8 -*-

from django.urls import re_path

from categories import views

urlpatterns = [
    re_path(r'^(?P<category>[\w-]+)$', views.category, name='view-category'),
]