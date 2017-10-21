from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get/images', views.images),
    url(r'^requestprayer', views.prayerrequest)
]
