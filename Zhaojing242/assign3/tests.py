from django.test import TestCase
from django.test.utils import setup_test_environment

from django.test import Client

setup_test_environment()

# create an instance of the client for our use
client = Client()