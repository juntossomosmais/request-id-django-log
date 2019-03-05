from django.http import HttpResponse
from django.conf import settings


def index(request):
    return HttpResponse(str(settings.MIDDLEWARE))
