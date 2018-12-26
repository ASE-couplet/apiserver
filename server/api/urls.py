from django.urls import path
from .views import *

urlpatterns = [
    path('upload', Upload.as_view(), name='upload'),
    path('result', Result.as_view(), name='result'),
]
