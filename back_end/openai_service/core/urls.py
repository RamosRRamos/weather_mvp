"""
Module: urls

This module defines URL patterns for the common app.

URL Patterns:
    - index: URL pattern for the index view.
"""

from django.urls import path

from . import views
from .views import PlaylistView, TaskStatusView

app_name = "core"
urlpatterns = [

    path('api/playlist/', PlaylistView.as_view(), name='playlist'),
    path('api/task/<str:task_id>/', TaskStatusView.as_view(), name='task_status'),

]
