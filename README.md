# Request ID Django Log

[![Build Status](https://travis-ci.com/juntossomosmais/request-id-django-log.svg?token=cfB1EHQmosyKPne1bPRP&branch=master)](https://travis-ci.com/juntossomosmais/request-id-django-log)

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

You have the follow options

```python
REQUEST_ID_CONFIG = {
    "REQUEST_ID_HEADER": "HTTP_X_REQUEST_ID",
    "GENERATE_REQUEST_ID_IF_NOT_FOUND": True,
    "RESPONSE_HEADER_REQUEST_ID": "HTTP_X_REQUEST_ID",
}
```
- `REQUEST_ID_HEADER` is the name of the header that will have the request_id received. Used when your system is not the first one in the chain.
- `GENERATE_REQUEST_ID_IF_NOT_FOUND` If true it will generate a request_id if the header is not found.
- `RESPONSE_HEADER_REQUEST_ID` What is the name of the response header that will have the value of the request_id.

## Supported Versions

- `python 2.7` with Django `1.8`, `1.9` and `1.11`
- `python 3.5`, `3.6` and `3.7` with Django `1.8`, `1.9`, `1.11`, `2.0` and `2.1`
