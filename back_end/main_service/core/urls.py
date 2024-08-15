"""
Module: urls

This module defines URL patterns for the common app.

URL Patterns:
    - index: URL pattern for the index view.
"""

from django.urls import path

from . import views
from .views import PlaylistView

app_name = "core"
urlpatterns = [

    path('get-playlist/', PlaylistView.as_view(), name='get-playlist'),

]
