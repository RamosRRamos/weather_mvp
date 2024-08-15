"""
Module: routes

This module defines the routes for the application, specifying the viewsets to handle different API endpoints.

Routes:
    Each route consists of a regular expression (regex) pattern, the associated viewset, and the basename.
"""

from core.views import WeatherAPIVIEW

routes = [
    {"regex": r"wheater_search", "viewset": WeatherAPIVIEW, "basename": "wheaterviewset"},
]
