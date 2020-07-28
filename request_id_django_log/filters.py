import logging

from django.conf import settings
from request_id_django_log import local_threading
from request_id_django_log.settings import NO_REQUEST_ID as EMPTY_FIELD


class RequestIDFilter(logging.Filter):
    def filter(self, record):
        record.request_id = getattr(local_threading, "request_id", EMPTY_FIELD)
        return True


class SessionIDFilter(logging.Filter):
    SESSION_ID_CONFIG = getattr(settings, "SESSION_ID_CONFIG", {})
    SESSION_ID_STORAGE = SESSION_ID_CONFIG.get("SESSION_ID_STORAGE", None)

    def filter(self, record):
        session_id_storage = self.SESSION_ID_CONFIG.get("SESSION_ID_STORAGE")

        session_id = (
            session_id_storage() if callable(session_id_storage) else session_id_storage
        )
        record.session_id = session_id or EMPTY_FIELD
        return True
