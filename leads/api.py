import requests 
import urllib

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.contrib import auth

from rest_framework.response import Response
from rest_framework import generics, parsers, authentication
from rest_framework import exceptions as rest_exceptions

from core import utils
from peekedin import settings

from .models import Lead, LeadEvent
from .serializers import LeadSerializer

class LeadListView(generics.ListCreateAPIView):
    '''
    Listing and creating leads
    '''
    parser_classes = (parsers.JSONParser,)
    serializer_class = LeadSerializer
    model = Lead

    def get_queryset(self):
        utils.is_authed(self.request.user, 'auth.list_leads')
        return Lead.objects.filter(owner=self.request.user)

    def pre_save(self, obj):
        obj.owner = self.request.user

    def post_save(self, obj, created=False):
        if created:
            url = settings.SNITCH_SERVICE_URL + urllib.quote(obj.url)
            print "URL: %s" % url
            req = requests.get(url)
            data = req.json()

            linkedin = data.get('linked_in_response', {})
            events = data.get('change_response', [])

            first_name = linkedin.get('firstName', '')
            last_name = linkedin.get('lastName', '')

            obj.name = first_name + ' ' + last_name
            obj.headline = linkedin.get('headline', '')
            obj.image_url = linkedin.get('pictureUrl', '')
            obj.email = linkedin.get('email', '')

            # Add initial "tracking" event
            obj.events.create(event_type='Now tracking...')

            print "Name: %s" % obj.name
            print "Headline: %s" % obj.headline
            print "Image url: %s" % obj.image_url
            print "Email: %s" % obj.email

            obj.save()

        return super(LeadListView, self).post_save(obj, created)

class LeadDetailView(generics.RetrieveDestroyAPIView):
    model = Lead
    serializer_class = LeadSerializer
