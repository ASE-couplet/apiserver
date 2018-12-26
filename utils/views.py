import json

from django.http import HttpResponse
from django.views import View

from .exceptions import ApiBaseException


class ApiView(View):
    """Base class for JSON API views.

    If `request.content_type` is JSON, the payload will be parsed and put into `request.JSON`.
    If a JSON-serializable object is returned, the response will be JSON with `status=200`.
    If an ApiBaseException is raised, the response will be an error response.
    """

    def dispatch(self, request, *args, **kwargs):
        if request.content_type == 'application/json':
            request.JSON = json.load(request)
        try:
            result = super().dispatch(request, *args, **kwargs)
        except ApiBaseException as e:
            return self.error(e.status, e.message)
        if isinstance(result, (dict, list, tuple, str, int, float, bool)):
            return HttpResponse(json.dumps(result).encode(), content_type='application/json')
        else:
            return result

    def error(self, status, message):
        payload = {'error': message}
        return HttpResponse(json.dumps(payload).encode(), status=status, content_type='application/json')
