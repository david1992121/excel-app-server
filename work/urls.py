"""
API URLs for Account
"""

from django.urls import path, include
from .views import *

urlpatterns = [
    path('ratios', get_ratio_list, name='ratios_list'),
    path('industries', get_industry_list, name='industries_list'),
    path('sheets', ClassesView.as_view(), name="sheets_view"),
    path('sheets/<int:pk>', ClassesView.as_view(), name="sheets_detail_view"),
    path('sheets/check', check_sheet_title),
]