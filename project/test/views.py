"""Test views."""

# Django
from django.http import HttpResponse


def hello(request):
    """View test"""

    return HttpResponse("Hello, everything its Ok.")

