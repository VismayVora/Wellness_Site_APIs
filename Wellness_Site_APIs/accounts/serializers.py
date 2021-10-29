from logs.serializers import DietLogSerializer,WorkoutLogSerializer,HealthDataSerializer
from rest_framework import serializers
from logs.models import DietLog,WorkoutLog
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    #DietLog = serializers.PrimaryKeyRelatedField(many=True, queryset=DietLog.objects.all())
    #WorkoutLog = serializers.PrimaryKeyRelatedField(many=True, queryset=WorkoutLog.objects.all())
    
    DietLog = DietLogSerializer(many=True, read_only = True)
    WorkoutLog = WorkoutLogSerializer(many=True, read_only = True)
    HealthData = HealthDataSerializer(read_only = True)

    class Meta:
        model = User
        fields = '__all__'