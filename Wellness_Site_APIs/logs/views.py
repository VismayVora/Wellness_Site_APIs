from django.shortcuts import render
#from accounts.models import Account
from rest_framework import renderers, viewsets, permissions
from rest_framework.response import Response

from logs.models import DietLog
from logs.serializers import DietLogSerializer #,AccountSerializer

# Create your views here.
class DietLogViewset(viewsets.ModelViewSet):
    queryset = DietLog.objects.all()
    serializer_class = DietLogSerializer
    #permission_classes = [permissions.IsAuthenticatedorReadOnly]

    #def perform_create(self,serializer):
        #serializer.save(owner = self.request.user)

#class AccountViewSet(viewset.ReadOnlyModelViewSet):
    #queryset = Account.objects.all()
    #serializer_class = AccountSerializer