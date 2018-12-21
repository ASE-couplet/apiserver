from django.http import HttpResponse
from .models import Order
import json

def result(request):
    if not request.GET:
        return HttpResponse("can't get an order")
    id = request.GET['order']
    o = Order.objects.get(id=id)
    if not o.poem:
        return HttpResponse("not finished")
    else:
        response = json.dumps({'tags':o.tags, 'poem':o.poem})
        return HttpResponse(response)


def upload(request):
    if not request.FILES:
        return HttpResponse("no image uploaded")
    image = request.FILES['image']
    o = Order(image=image)
    o.save()
    id = o.id
    return HttpResponse(id)