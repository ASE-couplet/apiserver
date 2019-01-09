from utils import exceptions
from .models import Order


class OrderService:
    def __init__(self, order):
        self._order = order

    @classmethod
    def create(cls, image):
        order = Order.objects.create(image=image)
        return cls(order)

    @classmethod
    def get(cls, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            raise exceptions.NotFound
        return cls(order)

    def json(self):
        return {
            'id': self.id,
            'poem': self.poem,
        }

    @property
    def id(self):
        return self._order.id

    @property
    def poem(self):
        if self._order.card and self._order.couplet_card:
            return self._order.poem
        else:
            return None

    @property
    def image_url(self):
        return self._order.image.url

    @property
    def card_url(self):
        return self._order.card.url
    
    @property
    def couplet_card_url(self):
        return self._order.couplet_card.url
