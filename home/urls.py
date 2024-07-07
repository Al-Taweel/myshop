# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals


from django.urls import re_path

from home import views

urlpatterns = [
    re_path(r'^$', views.homepage, name='homepage'),
]