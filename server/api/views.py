from django.http import HttpResponsePermanentRedirect
from django.utils.datastructures import MultiValueDictKeyError

from utils.exceptions import BadRequest
from utils.views import ApiView
from .services import OrderService


class Upload(ApiView):
    def post(self, request):
        try:
            image = request.FILES['image']
        except MultiValueDictKeyError:
            raise BadRequest
        order = OrderService.create(image)
        return order.json()


class Result(ApiView):
    def get(self, request):
        try:
            id = request.GET['order']
        except MultiValueDictKeyError:
            raise BadRequest
        order = OrderService.get(id)
        return order.json()


class Image(ApiView):
    def get(self, request):
        try:
            id = request.GET['order']
        except MultiValueDictKeyError:
            raise BadRequest
        order = OrderService.get(id)
        return HttpResponsePermanentRedirect(order.image_url)
