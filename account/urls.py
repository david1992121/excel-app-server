"""
API URLs for Account
"""

from django.urls import path, include
from .views import *

urlpatterns = [
    path('register', register, name='user_register'),
    path('login', obtain_expiring_auth_token, name='api_token_auth')
]