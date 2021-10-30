from django.shortcuts import render
from accounts.models import create_auth_token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.http import JsonResponse,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import AllowAny

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
@api_view(['POST',])
@permission_classes([AllowAny])
def register_view(request):

    if request.method == 'POST':
        serializer = UserSerializer(data = request.data) 
        data = {}
        if serializer.is_valid():
            User = serializer.save()
            data['username'] = User.email
            token = Token.objects.get(user = User).key
            data['token'] = token

            #Creating Verification Link
            domain_link = get_current_site(request).domain
            continued_link = reverse('Verification')
            verification_link = 'http://' + domain_link + continued_link + '?token=' + token

            subject = 'Verification of your account for the Wellnes Site!'
            from_email = 'voravismay99@gmail.com'
            to_email = [serializer.validated_data['email'], ]
            body = 'Thank You for joining us! Click on this link to verify your account. Link: {}'.format(verification_link)
            send_mail(subject, body, from_email, to_email, fail_silently=False)
            
            data['Message'] = "You have been successfully registered.Check your email for the verification link! {}".format(to_email)


        
        else:
            data = serializer.errors
            
    else:
        data = serializer.errors
    return JsonResponse(data)

@api_view(['GET',])
def verification_view(request):

    if request.method == 'GET':
        token = request.GET.get('token')
        user = User.objects.get(auth_token = token)
        if not user.is_active:
            user.is_active = True
            user.auth_token.delete()
            Token.objects.create(user = user)
            user.save()
    return Response('Your account has been successfully verified', status=status.HTTP_200_OK)

