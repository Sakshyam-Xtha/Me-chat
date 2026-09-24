from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
@api_view(["GET"])
def health(request):
    return Response({"status":200})

@api_view(["POST"])
def register(request):
    username = request.data["name"]  # This should ideally come from the request data
    email = request.data["email"]  # This should also come from the request data
    password = make_password(request.data["pwd"])
    
    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        return Response({"msg": "error", "details": "Username already exists."})

    new_user = User(username=username, email=email, password=password, role="user")
    try:
        new_user.save()
        return Response({"msg": "new user created"})
    except Exception as e:
        return Response({"msg": "error", "details": str(e)})
    
@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_lists(request):
    if request.method == "GET":
        return Response({"msg":"Can be accessed by all"})
    elif request.method == "POST":
        return Response({"msg":f"Data created by {request.user.username}"})