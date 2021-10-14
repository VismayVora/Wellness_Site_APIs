from rest_framework import serializers

from logss.models import DietLog

class DietLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietLog
        fields = '__all__'