from django.urls import path
from .views import *

urlpatterns = [
    path('upload', Upload.as_view(), name='upload'),
    path('result', Result.as_view(), name='result'),
    path('image', Image.as_view(), name='image'),
    path('card', Card.as_view(), name='card'),
    path('couplet_card', Couplet_card.as_view(), name='couplet_card'),
    path('evaluate', Evaluate.as_view(), name="evaluate")
]
