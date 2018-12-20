import json
import random

from django.shortcuts import render
from django.http import HttpResponse

from api.models import Order


def upload(request):
    if request.method == 'POST':
        image = request.FILES['image']
        id = random.randint(0,100000)
        o = Order(id=id, image=image)
        o.save()
        return HttpResponse(json.dumps({'id':id}))
    else:
        return HttpResponse('bad request')
        
def result(request):
    if request.method == 'GET':
        id_dict = request.GET['order']
        o = Order.objects.get(id=id_dict['id'])
        if o.poem:
            return HttpResponse(json.dumps({'poem':o.poem}))
        else:
            return HttpResponse('not finished')
    else:
        return HttpResponse('wrong request')
        