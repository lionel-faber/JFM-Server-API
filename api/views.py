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
    sender = request.POST.get('sender_name')
    message = request.POST.get('prayer_request')
    phone_no =request.POST.get('phone_no')
    request = PrayerRequests(sender = sender, phone = phone_no, message = message)
    request.save()
    return HttpResponse("Prayer Request Sent")
