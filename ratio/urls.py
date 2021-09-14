"""
API URLs for Account
"""

from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_list, name='ratios_list')
]