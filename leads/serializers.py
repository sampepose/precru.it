from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Lead, LeadEvent

class LeadEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadEvent
        exclude = ('lead',)

class LeadSerializer(serializers.ModelSerializer):
    events = LeadEventSerializer(many=True, required=False)

    class Meta:
        model = Lead
        exclude = ('owner',)

