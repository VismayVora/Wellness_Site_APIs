from django.shortcuts import render
from rest_framework import renderers, viewsets, permissions, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
User = get_user_model()

from logs.models import DietLog, WorkoutLog, HealthData
from logs.serializers import DietLogSerializer, WorkoutLogSerializer, HealthDataSerializer
from accounts.serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DietLogViewSet(viewsets.ModelViewSet):
    queryset = DietLog.objects.all()
    serializer_class = DietLogSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        return DietLog.objects.filter(owner=self.request.user)

    def perform_create(self,serializer):
        serializer.save(owner = self.request.user)

class WorkoutLogViewSet(viewsets.ModelViewSet):
    queryset = WorkoutLog.objects.all()
    serializer_class = WorkoutLogSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        return WorkoutLog.objects.filter(owner=self.request.user)

    def perform_create(self,serializer):
        serializer.save(owner = self.request.user)


class HealthDataAPIView(viewsets.ModelViewSet):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HealthData.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


