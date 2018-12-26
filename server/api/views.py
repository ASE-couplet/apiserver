import json

from django.http import HttpResponse

from .models import Order


def result(request):
    if not request.GET:
        response = json.dumps({'error': "can't get an order"})
        return HttpResponse(content=response, content_type='application/json', status=404)
    id = request.GET['order']
    o = Order.objects.get(id=id)
    if not o.poem:
        response = json.dumps({'id': o.id, 'poem': None})
        return HttpResponse(content=response, content_type='application/json', status=200)
    else:
        response = json.dumps({'id': o.id, 'poem': o.poem})
        return HttpResponse(content=response, content_type='application/json', status=200)


def upload(request):
    if not request.FILES:
        response = json.dumps({'error': 'no image uploaded'})
        return HttpResponse(content=response, content_type='application/json', status=415)
    image = request.FILES['image']
    o = Order(image=image)
    o.save()
    response = json.dumps({'id': o.id})
    return HttpResponse(content=response, content_type='application/json', status=200)
