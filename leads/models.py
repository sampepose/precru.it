from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    # The user who owns this lead
    owner = models.ForeignKey(User, related_name='leads')

    # name of the lead
    name = models.CharField(max_length=64)

    # headline of the lead
    name = models.CharField(max_length=64)

    # email of the lead
    email = models.EmailField()

    # LinkedIn profile URL
    url = models.URLField()

    # LinkedIn image URL
    image_url = models.URLField()

class LeadEvent(models.Model):
    # Lead this event belongs to
    lead = models.ForeignKey(Lead)

    # Event type (field that changed)
    event_type = models.CharField(max_length=64)

    event_datetime = models.DateTimeField(auto_now=True, auto_now_add=True) 
