from request_id_django_log.settings import NO_REQUEST_ID
from request_id_django_log import local_threading


def current_request_id():
    try:
        return local_threading.request_id
    except AttributeError:
        return NO_REQUEST_ID
