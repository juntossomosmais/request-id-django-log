import logging

from request_id_django_log import local_threading
from request_id_django_log.settings import NO_REQUEST_ID


class RequestIDFilter(logging.Filter):
    def filter(self, record):
        record.request_id = getattr(local_threading, "request_id", NO_REQUEST_ID)
        return True
