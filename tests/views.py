from django.conf import settings
from django.http import HttpResponse


def index(request):
    return HttpResponse(str(settings.MIDDLEWARE))
