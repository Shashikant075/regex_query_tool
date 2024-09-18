from django.urls import path
from .views import regex_query, download_csv, download_pdf

urlpatterns = [
    path('', regex_query, name='regex_query'),
    path('download_csv/', download_csv, name='download_csv'),
    path('download_pdf/', download_pdf, name='download_pdf'),
]