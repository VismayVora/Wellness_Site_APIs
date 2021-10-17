from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from accounts.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

# Create your views here.
@api_view(['POST',])

def register_view(request):

    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            User = serializer.save()
            data['response'] = "User has been successfully registered."
            data['username'] = User.email
            token = Token.objects.get(user = User).key
            data['token'] = token
        else:
            data = serializer.errors
        return JsonResponse(data)
