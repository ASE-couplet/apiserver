from django.urls import path
from .views import *

urlpatterns = [
    path('upload', Upload.as_view(), name='upload'),
    path('result', Result.as_view(), name='result'),
    path('image', Image.as_view(), name='image'),
    path('card', Card.as_view(), name='card'),
]
