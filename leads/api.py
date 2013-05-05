from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.contrib import auth

from rest_framework.response import Response
from rest_framework import generics, parsers
from rest_framework import exceptions as rest_exceptions

from .models import Lead, LeadEvent
from .serializers import LeadSerializer

class LeadListView(generics.ListCreateAPIView):
    '''
    Listing and creating leads
    '''
    if not request.user.is_authenticated():
        raise rest_exceptions.PermissionDenied()
    elif not request.user.has_perm("list_leads"):
        raise rest_exceptions.PermissionDenied()
    else:
        pass
        
    parser_classes = (parsers.JSONParser,)
    serializer_class = LeadSerializer
    model = Lead

    def get_queryset(self):
        return Lead.objects.filter(owner=self.request.user)

    def pre_save(self, obj):
        obj.owner = self.request.user
