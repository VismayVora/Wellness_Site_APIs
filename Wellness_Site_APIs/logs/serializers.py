from rest_framework import serializers

from logs.models import DietLog,WorkoutLog#HealthData


class DietLogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.email')
    
    class Meta:
        model = DietLog
        fields = '__all__'


class WorkoutLogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.email')
    
    class Meta:
        model = WorkoutLog
        fields = '__all__'

'''
class HealthDataSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.email')
    bmi = serializers.SerializerMethodField()

    class Meta:
        model = HealthData
        fields = '__all__'
    
    def get_bmi(self,obj):
        #weight = HealthData.weight
        #height = HealthData.height
        bmi = obj.weight/((obj.height/100)**2)
        bmi = round(bmi,2)
        return bmi

'''
