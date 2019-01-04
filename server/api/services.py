from utils import exceptions
from .models import Order
from django.db.models import Max


class OrderService:
    def __init__(self, order):
        self._order = order

    @classmethod
    def create(cls, image, type):
        order = Order.objects.create(image=image, type=type)
        return cls(order)

    @classmethod
    def get(cls, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            raise exceptions.NotFound
        return cls(order)

    # def json(self):
    #     return {
    #         'id': self.id,
    #         'poem': self.poem,
    #     }

    def json(self):
        return {
            'id': self._order.id,
            'poem': self._order.poem_set.all().get(index__exact=1)
        }

    @property
    def id(self):
        return self._order.id

    @property
    def poem(self):
        return self._order.poem

    @property
    def image_url(self):
        return self._order.image.url

    # @property
    # def card_url(self):
    #     return self._order.card.url

    @property
    def couplet_maxIdx(self):
        maxIdx = self._order.couplet_set.all().aggregate(Max('index'))
        return maxIdx['index__max']

    @property
    def poem_maxIdx(self):
        maxIdx = self._order.poem_set.all().aggregate(Max('index'))
        return maxIdx['index__max']

    def couplet_url(self, idx):
        couplet = self._order.couplet_set.all().get(index__exact=idx)
        return couplet.card.url

    def poem_url(self, idx):
        poem = self._order.poem_set.all().get(index__exact=idx)
        return poem.card.url 
