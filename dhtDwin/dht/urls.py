from django.contrib import admin
from django.urls import path, include

from .views import TempHumCreateAPIView, TempHumListAPIView, StatusPost

urlpatterns = [
    path('api/temphum/create/', TempHumCreateAPIView.as_view(), name='temphum-create'),
    path('api/temphum/list/', TempHumListAPIView.as_view(), name='temphum-create'),
    path('api/status/', StatusPost.as_view(), name='status'),


]