from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework_swagger.renderers import SwaggerUIRenderer

from collections import OrderedDict


def swagger_json(requests):
    import json
    from collections import OrderedDict
    with open('main/swagger.json', 'r') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
    return HttpResponse(json.dumps(data, indent=4),
                        content_type='application/json')


class CustomSwaggerUIRenderer(SwaggerUIRenderer):
    def get_ui_settings(self):
        data = super().get_ui_settings()
        data['url'] = reverse('swagger_json')
        return data

@api_view()
@renderer_classes([CustomSwaggerUIRenderer])
def swagger_view(request):
    return Response()


@api_view(['GET'])
@permission_classes([])
def api_root(request, format=None):
    return Response(OrderedDict([
        ('swagger', reverse('swagger', request=request, format=format)),
        ('swagger_json', reverse('swagger_json', request=request, format=format)),
        ('auth-login', reverse('auth-login', request=request, format=format)),
        ('auth-logout', reverse('auth-logout', request=request, format=format)),
        ('auth-password', reverse('auth-password', request=request, format=format)),
        ('problems', reverse('problem-list', request=request, format=format)),
        ('submits', reverse('submit-list', request=request, format=format)),
        ('my-info', reverse('my-info', request=request, format=format)),
        ('my-submits', reverse('my-submit-list', request=request, format=format)),
    ]))
