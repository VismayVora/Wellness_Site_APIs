from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST',])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def register_view(request):

    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            User = serializer.save()
            data['response'] = "User has been successfully registered."
            data['username'] = User.email
            token = Token.objects.get(user = User).key
            data['token'] = Token
        else:
            data = serializer.errors
        return Response(data)
