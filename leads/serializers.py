from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Lead, LeadEvent

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
