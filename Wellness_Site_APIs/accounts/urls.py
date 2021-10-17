from django.urls import path,include
from accounts.views import register_view
from accounts import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', register_view, name = 'Register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]