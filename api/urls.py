from django.urls import include, path
from rest_framework import routers
from . import views
from .views import checkNumber

urlpatterns = [
    path('checknumber/', checkNumber.as_view() ),

]