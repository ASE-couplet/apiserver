from django.http import HttpResponsePermanentRedirect
from django.utils.datastructures import MultiValueDictKeyError

from utils.exceptions import BadRequest, NotFound
from utils.views import ApiView, CsrfExemptMixin
from .services import OrderService

class Evaluate(ApiView):
    def get(self, request):
        try:
            id = request.GET['order']
            score = request.GET['evaluate']
            f = open('./evaluate.txt', 'a')
            f.write('{}\t{}\n'.format(str(id), score))
        except:
            pass

def FaceTypeUpload(CsrfExemptMixin, ApiView):
    def post(self, request):
        try:
            image = request.FILES['image']
        except MultiValueDictKeyError:
            raise BadRequest
        order = OrderService.create_face_type(image)
        return order.json()

class Upload(CsrfExemptMixin, ApiView):
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


class Card(ApiView):
    def get(self, request):
        try:
            id = request.GET['order']
        except MultiValueDictKeyError:
            raise BadRequest
        order = OrderService.get(id)
        if not order.poem:
            raise NotFound
        return HttpResponsePermanentRedirect(order.card_url)


class Couplet_card(ApiView):
    def get(self, request):
        try:
            id = request.GET['order']
        except MultiValueDictKeyError:
            raise BadRequest
        order = OrderService.get(id)
        if not order.poem:
            raise NotFound
        return HttpResponsePermanentRedirect(order.couplet_card_url)
        
