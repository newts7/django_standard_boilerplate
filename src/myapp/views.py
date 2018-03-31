from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import  logging
from myproject.settings import *
from django.core.mail import send_mail

# Create your views here.

logger = logging.getLogger('__name__')

def index(request):
    print(MAILER_LIST)
    print(lehsun)
    send_mail('Testing','Khilauna Mati ka',DEFAULT_FROM_EMAIL, MAILER_LIST, fail_silently = False)
    return HttpResponse({'Hello World'},status=200)