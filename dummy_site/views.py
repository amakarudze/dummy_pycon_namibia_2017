from django.shortcuts import render
from django.http import HttpRequest

from datetime import datetime


"""Renders the home page"""
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'dummy_site/index.html',
        {
            'title': 'Home Page',
            'message': 'Home Page.',
            'year': datetime.now().year,
        }
    )
