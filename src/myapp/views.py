from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    return HttpResponse({'Hello World'},status=200)
