from django.http import HttpResponsePermanentRedirect
from django.utils.datastructures import MultiValueDictKeyError

from utils.exceptions import BadRequest, NotFound
from utils.views import ApiView, CsrfExemptMixin
from .services import OrderService


class Upload(CsrfExemptMixin, ApiView):
    def post(self, request):
        try:
            image = request.FILES['image']
        except MultiValueDictKeyError:
            raise BadRequest
        try:
            type = request.POST.get('type')
        except MultiValueDictKeyError:
            type = 'landscape'
        order = OrderService.create(image, type)
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


class Card(ApiView):
    def get(self, request):
        try:
            id = request.GET['order']
        except MultiValueDictKeyError:
            raise BadRequest
        order = OrderService.get(id)
        maxIdx = order.poem_maxIdx
        if maxIdx < 1:
            raise NotFound
        else:
            return HttpResponsePermanentRedirect(order.poem_url(1))


class Couplet(ApiView):
    def get(self, request):
        try:
            id = request.GET['order']
        except MultiValueDictKeyError:
            raise BadRequest
        try:
            idx = request.GET['index']
        except MultiValueDictKeyError:
            idx = 1
        order = OrderService.get(id)
        maxIdx = order.couplet_maxIdx
        if maxIdx < idx:
            raise NotFound
        else:
            return HttpResponsePermanentRedirect(order.couplet_url(idx))
            
            
class Poem(ApiView):
    def get(self, request):
        try:
            id = request.GET['order']
        except MultiValueDictKeyError:
            raise BadRequest
        try:
            idx = request.GET['index']
        except MultiValueDictKeyError:
            idx = 1
        order = OrderService.get(id)
        maxIdx = order.poem_maxIdx
        if maxIdx <idx:
            raise NotFound
        else:
            return HttpResponsePermanentRedirect(order.poem_url(idx))
        