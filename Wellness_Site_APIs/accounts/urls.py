from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
path('auth/', include('rest_auth.urls')),
path(" ", include("account.urls")),
]
