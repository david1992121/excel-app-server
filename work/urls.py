"""
API URLs for Account
"""

from django.urls import path, include
from .views import *

urlpatterns = [
    path('ratios', get_ratio_list, name='ratios_list'),
    path('industries', get_industry_list, name='industries_list'),
    path('sheets', SheetsView.as_view(), name="sheets_view"),
    path('sheets/<int:pk>', SheetsDetailView.as_view(), name="sheets_detail_view"),
    path('sheets/check', check_sheet_title, name="sheets_title_check"),
]
