from rest_framework import serializers

from logs.models import DietLog,WorkoutLog


class DietLogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = DietLog
        fields = '__all__'

class WorkoutLogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = WorkoutLog
        fields = '__all__'
