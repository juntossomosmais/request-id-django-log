# Request ID Django Log

[![Build Status](https://travis-ci.com/juntossomosmais/request-id-django-log.svg?token=cfB1EHQmosyKPne1bPRP&branch=master)](https://travis-ci.com/juntossomosmais/request-id-django-log) [![Maintainability](https://api.codeclimate.com/v1/badges/bb134244b75f5e0a8893/maintainability)](https://codeclimate.com/github/juntossomosmais/request-id-django-log/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/bb134244b75f5e0a8893/test_coverage)](https://codeclimate.com/github/juntossomosmais/request-id-django-log/test_coverage) [![Coverage Status](https://coveralls.io/repos/github/juntossomosmais/request-id-django-log/badge.svg?branch=master)](https://coveralls.io/github/juntossomosmais/request-id-django-log?branch=master) [![PyPI version](https://badge.fury.io/py/request-id-django-log.svg)](https://badge.fury.io/py/request-id-django-log) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Downloads](https://pepy.tech/badge/request-id-django-log)](https://pepy.tech/project/request-id-django-log) [![Downloads](https://pepy.tech/badge/request-id-django-log/month)](https://pepy.tech/project/request-id-django-log) [![Downloads](https://pepy.tech/badge/request-id-django-log/week)](https://pepy.tech/project/request-id-django-log)
 [![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/ricardochaves)

## Install

`pip install request-id-django-log`

Update your `INSTALLED_APPS` and `MIDDLEWARE`
```python
INSTALLED_APPS = [
    ...
    "request_id_django_log",
]
```

```python
MIDDLEWARE = [
    ...
    "request_id_django_log.middleware.RequestIdDjangoLog",
]
```

## Configure

The following options are used by this library:

```python
REQUEST_ID_CONFIG = {
    "REQUEST_ID_HEADER": "HTTP_X_REQUEST_ID",
    "GENERATE_REQUEST_ID_IF_NOT_FOUND": True,
    "RESPONSE_HEADER_REQUEST_ID": "HTTP_X_REQUEST_ID",
}
```

- `REQUEST_ID_HEADER` is the header name which will hold the received request_id. This must be used when another system is responsible for generating the request_ids and sending them to your django application.
- `GENERATE_REQUEST_ID_IF_NOT_FOUND` If set to true, a new request_id will be generated if none was previously supplied.
- `RESPONSE_HEADER_REQUEST_ID` sets the name of the response header which will hold the value of the request_id.

## Supported Versions

- `python 2.7` with Django `1.8`, `1.9` and `1.11`
- `python 3.5`, `3.6` and `3.7` with Django `1.8`, `1.9`, `1.11`, `2.0` and `2.1`
