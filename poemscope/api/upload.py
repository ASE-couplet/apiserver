from django.http import HttpResponse
import random
from .models import Order
import json

def upload(request):
    if not request.FILES:
        return HttpResponse("no image uploaded")
    image = request.FILES['image']
    id = random.randint(1, 10000000)
    o = Order(id=id, image=image)
    o.save()
    # return HttpResponse(json.dumps({'id':id}))
    return HttpResponse(id)
