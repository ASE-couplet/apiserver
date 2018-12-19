from django.urls import path
from . import upload, result
urlpatterns = [
    path('upload',upload.upload, name='upload'),
    path('result',result.result, name='result')
]
