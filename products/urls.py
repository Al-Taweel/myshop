# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from django.urls import re_path, include

from products import views


urlpatterns = [
    re_path(r'^(?P<product_slug>[\w-]+)$', views.product_view, name='view-product'),
]