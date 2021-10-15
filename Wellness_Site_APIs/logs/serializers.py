from rest_framework import serializers

from logs.models import DietLog
#from accounts.models import Account

class DietLogSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source = owner.username)
    class Meta:
        model = DietLog
        fields = '__all__'

#class AccountSerializer(serializer.HyperLinkedModelSerializer):
    #DietLog = serializers.HyperlinkedRelatedField(many = True, view_name = 'DietLog-detail', read_only = True)

    #class Meta:
        #model = Account
        #fields = '__all__'
