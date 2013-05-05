from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    # The user who owns this lead
    owner = models.ForeignKey(User, related_name='leads')

    # name of the lead
    name = models.CharField(max_length=64, blank=True)

    # headline of the lead
    headline = models.CharField(max_length=64, blank=True)

    # email of the lead
    email = models.EmailField(blank=True)

    # LinkedIn profile URL - unique!
    url = models.URLField(unique=True)

    # LinkedIn image URL
    image_url = models.URLField(blank=True)

class LeadEvent(models.Model):
    # Lead this event belongs to
    lead = models.ForeignKey(Lead, related_name='events')

    # Event type (field that changed)
    event_type = models.CharField(max_length=64)

    event_datetime = models.DateTimeField(auto_now=True, auto_now_add=True) 
