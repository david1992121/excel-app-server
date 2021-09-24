"""
API URLs for Account
"""

from django.urls import path, include
from .views import *

urlpatterns = [
    path('register', register, name='user_register'),
    path('login', obtain_expiring_auth_token, name='api_token_auth'),
    path('info', get_info, name='user_info'),
    path('bulk', bulk_create, name='bulk_create')
]