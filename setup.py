import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="request_id_django_log",
    version="0.0.1",
    description="A simple way to implement request_id in Django",
    long_description=README,
    include_package_data=True,
    author="Ricardo Baltazar Chaves",
    author_email="ricardobchaves6@gmail.com",
    license="MIT",
    url="https://github.com/juntossomosmais/request-id-django-log",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Environment :: Web Environment",
        "Natural Language :: Portuguese (Brazilian)",
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
