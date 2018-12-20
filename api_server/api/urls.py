from django.urls import path
from . import views

urlpatterns = [
    path('result/', views.result),
    path('upload/', views.upload),
    ]