from django.shortcuts import render
from rest_framework import renderers, viewsets, permissions, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
User = get_user_model()

from logs.models import DietLog, WorkoutLog, HealthData
from logs.serializers import DietLogSerializer, WorkoutLogSerializer, HealthDataSerializer
from accounts.serializers import UserSerializer

from rest_framework import status
from django.http.response import Http404

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

class HealthDataAPIView(APIView):   
    def get_object(self,pk):
        try:
            return HealthData.objects.get(pk=self.request.user)
        except HealthData.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        healthdata = self.get_object(pk =self.request.user)
        serializer = HealthDataSerializer(healthdata)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = HealthDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        instance = self.get_object(pk = self.request.user)
        serializer = HealthDataSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        healthdata = self.get_object(pk = self.request.user)
        healthdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
#As a ModelViewSet
class HealthDataAPIView(viewsets.ModelViewSet):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HealthData.objects.filter(owner=self.request.user)
    
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(pk=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def perform_update(self,serializer):
        instance = serializer.save()
'''


