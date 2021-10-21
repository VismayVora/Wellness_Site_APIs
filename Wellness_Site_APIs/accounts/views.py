from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from accounts.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.http import JsonResponse,HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
@api_view(['POST',])

def register_view(request):

    if request.method == 'POST':
        serializer = UserSerializer(data = request.data) 
        data = {}
        if serializer.is_valid():
            #User = serializer.save()
            #data['response'] = "User has been successfully registered."
            #data['username'] = User.email
            #token = Token.objects.get(user = User).key
            #data['token'] = token
            global registration_data
            def registration_data():
                return serializer
            send_mail('Verification of your Account','Thank You for joining us! Copy-paste this link and continue to create your account. Link: " http://127.0.0.1:8000/verify/ " ','voravismay99@gmail.com',[serializer.validated_data['email'],], fail_silently=False)
            data['Message'] = "Check your email! {}".format(serializer.validated_data['email'])
        else:
            data = serializer.errors
        return JsonResponse(data)

@api_view(['GET',])
def verification_view(request):

    if request.method == 'GET':
        serializer = registration_data()
        data = {}
        if serializer.is_valid():
            User = serializer.save()
            data['response'] = "User has been successfully registered."
            data['username'] = User.email
            token = Token.objects.get(user = User).key
            data['token'] = token
            #send_mail('Verification of your Account','Thank You for joining us! Copy-paste this link to create your account.','voravismay99@gmail.com',[User.email,], fail_silently=False)
        else:
            data = serializer.errors
        return JsonResponse(data)
