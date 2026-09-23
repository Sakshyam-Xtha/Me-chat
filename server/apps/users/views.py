from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def health(request):
    return JsonResponse({"status":200})

@api_view(["POST"])
def register(request):
    username = request.data["name"]  # This should ideally come from the request data
    email = request.data["email"]  # This should also come from the request data
    password = make_password(request.data["pwd"])
    
    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        return JsonResponse({"msg": "error", "details": "Username already exists."})

    new_user = User(username=username, email=email, password=password, role="user")
    try:
        new_user.save()
        return JsonResponse({"msg": "new user created"})
    except Exception as e:
        return JsonResponse({"msg": "error", "details": str(e)})