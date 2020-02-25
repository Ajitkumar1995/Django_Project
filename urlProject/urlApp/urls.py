from django.urls import path
from urlApp import views

urlpatterns=[
    path('test/',views.appurlinfo)
]