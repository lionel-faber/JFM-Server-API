# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def images(request):
    s = ImageLink.objects.all().values()
    links = list(s)
    return JsonResponse(links, safe=False)

@csrf_exempt
def prayerrequest(request):
    subject = "Prayer Request from " + request.POST['sender_name']
    message = request.POST['prayer_request'] + " " + request.POST['phone_no']
    send_mail(subject, message, 'aca.jfm.pjcr@gmail.com', ['lionel1704@gmail.com'], fail_silently=False)
    return HttpResponse("Prayer Request Sent")
