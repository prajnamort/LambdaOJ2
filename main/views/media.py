import os
import magic

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.conf import settings

from rules import test_rule


def serve_media(request, name):
    if not test_rule('can_access_media_files', request.user):
        return HttpResponseForbidden()

    path = '{}{}'.format(settings.MEDIA_ROOT, name)
    if os.path.exists(path) and os.path.isfile(path):
        mime = magic.Magic(mime=True)
        with open(path, 'rb') as f:
            response = HttpResponse(f)
            response['Content-Type'] = mime.from_file(path)
            response['Content-Disposition'] = 'attachment'
            return response
    else:
        return HttpResponseNotFound()
