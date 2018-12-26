from django.utils.datastructures import MultiValueDictKeyError

from utils.exceptions import *
from utils.views import ApiView
from .models import Order


class Upload(ApiView):
    def post(self, request):
        try:
            image = request.FILES['image']
        except MultiValueDictKeyError:
            raise BadRequest
        order = Order.objects.create(image=image)
        return {'id': order.id}


class Result(ApiView):
    def get(self, request):
        try:
            id = request.GET['order']
        except MultiValueDictKeyError:
            raise BadRequest
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            raise NotFound
        return {'id': order.id, 'poem': order.poem}
