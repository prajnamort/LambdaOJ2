from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.response import Response

from collections import OrderedDict


@api_view(['GET'])
@permission_classes([])
def api_root(request, format=None):
    return Response(OrderedDict([
        ('auth_login', reverse('auth_login', request=request, format=format)),
        ('auth_logout', reverse('auth_logout', request=request, format=format)),
        ('auth_password', reverse('auth_password', request=request, format=format)),
        ('problems', reverse('problem-list', request=request, format=format)),
        ('submits', reverse('submit-list', request=request, format=format)),
        ('my-info', reverse('my-info', request=request, format=format)),
    ]))
