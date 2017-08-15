from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([])
def api_root(request, format=None):
    return Response({
        'problems': reverse('problem-list', request=request, format=format),
    })
