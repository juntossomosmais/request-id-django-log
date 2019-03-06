import uuid

from django.test import TestCase

from request_id_django_log import local_threading
from request_id_django_log.apps import RequestIdDjangoLogConfig
from request_id_django_log.filters import RequestIDFilter
from request_id_django_log.middleware import RequestIdDjangoLog
from request_id_django_log.request_id import current_request_id

try:
    from unittest.mock import MagicMock, patch
except ImportError:
    from mock import MagicMock, patch


class RequestIDTestCase(TestCase):
    def setUp(self):
        pass

    def test_app(self):
        "APP: Shoud return app name request_id_django_log when RequestIdDjangoLogConfig exists"
        self.assertEqual(RequestIdDjangoLogConfig.name, "request_id_django_log")

    def test_filters_should_return_none(self):
        """Filter: Should return none when local_threading dont have request_id"""
        mock_record = MagicMock()
        filter = RequestIDFilter(MagicMock())
        result = filter.filter(mock_record)

        self.assertEqual(mock_record.request_id, "none")
        self.assertTrue(result)
        self.assertIsInstance(filter, RequestIDFilter)

    def test_filters_should_return_id(self):
        """Filter: Should return request_id when local_threading have request_id"""
        local_threading.request_id = "12345"
        mock_record = MagicMock()
        filter = RequestIDFilter(MagicMock())

        result = filter.filter(mock_record)
        del local_threading.request_id

        self.assertEqual(mock_record.request_id, "12345")
        self.assertTrue(result)
        self.assertIsInstance(filter, RequestIDFilter)

    def test_middleware_get_request_id_return_id_from_header(self):
        """Middleware: Should return request_id equals header when header request_id is present"""
        mock_request = MagicMock()
        mock_request.META = {"request_is": "123"}

        mid = RequestIdDjangoLog()
        request_id = mid._get_request_id(
            mock_request, {"REQUEST_ID_HEADER": "request_is"}
        )

        self.assertEqual(request_id, "123")

    def test_middleware_get_request_id_generate_id_header_not_found(self):
        """Middleware: Should return generated request_id when config header not found"""
        mock_request = MagicMock()

        mid = RequestIdDjangoLog()
        request_id = mid._get_request_id(mock_request, {})

        self.assertTrue(uuid.UUID(request_id))

    def test_middleware_get_request_id_generate_id_request_header_not_found(self):
        """Middleware: Should return request_id equals header when header request_id is present"""
        mock_request = MagicMock()
        mock_request.META = {}

        configs = {
            "REQUEST_ID_HEADER": "request_is",
            "GENERATE_REQUEST_ID_IF_NOT_FOUND": True,
        }

        mid = RequestIdDjangoLog()
        request_id = mid._get_request_id(mock_request, configs)

        self.assertTrue(uuid.UUID(request_id))

    def test_middleware_get_request_id_none_when_not_need_generate(self):
        """Middleware: Should return request_id none when generate config not found"""
        mock_request = MagicMock()
        mock_request.META = {}
        mid = RequestIdDjangoLog()
        request_id = mid._get_request_id(
            mock_request, {"REQUEST_ID_HEADER": "request_is"}
        )

        self.assertEqual(request_id, "none")

    def test_local_threading_return_id(self):
        """Current Request ID: Should return 123 when local_thead have value"""

        local_threading.request_id = "123"
        self.assertEqual(current_request_id(), "123")
        del local_threading.request_id

    def test_local_threading_return_none(self):
        """Current Request ID: Should return none when local_thead dont have value"""

        self.assertEqual(current_request_id(), "none")
