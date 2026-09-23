from django.urls import path, include
from apps.users import views

urlpatterns = [
    path('health/',views.health),
    path('register/',views.register),
]