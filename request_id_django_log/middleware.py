import uuid

from django.conf import settings

from request_id_django_log import local_threading
from request_id_django_log.settings import NO_REQUEST_ID

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class RequestIdDjangoLog(MiddlewareMixin):
    def process_request(self, request):
        configs = getattr(settings, "REQUEST_ID_CONFIG", None)
        if configs:
            request_id = self._get_request_id(request, configs)
            request.id = request_id
            local_threading.request_id = request_id

    def process_response(self, request, response):
        configs = getattr(settings, "REQUEST_ID_CONFIG", None)
        if not configs:
            return response

        if configs.get("RESPONSE_HEADER_REQUEST_ID", False):
            response[configs.get("RESPONSE_HEADER_REQUEST_ID")] = request.id

        return response

    def _get_request_id(self, request, configs):
        header = configs.get("REQUEST_ID_HEADER", None)

        generate_request_if_not_found = configs.get(
            "GENERATE_REQUEST_ID_IF_NOT_FOUND", False
        )

        if header:
            default = NO_REQUEST_ID

            if generate_request_if_not_found:
                default = self._generate_id()

            return request.META.get(header, default)

        return self._generate_id()

    @staticmethod
    def _generate_id():
        return str(uuid.uuid4())
