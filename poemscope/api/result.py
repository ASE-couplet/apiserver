from django.http import HttpResponse
from .models import Order
import json

def result(request):
    if not request.GET:
        return HttpResponse("can't get an order")
    id = request.GET['order']
    o = Order.objects.get(id=id)
    if not o.poem:
        # response = json.dumps({'response':'not finished'})
        # return HttpResponse(response)
        return HttpResponse("not finished")
    else:
        response = json.dumps({'tags':o.tags, 'poem':o.poem})
        return HttpResponse(response)
