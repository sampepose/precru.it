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

    def update_snitch(self, lead_obj, initial=False):
        url = settings.SNITCH_SERVICE_URL + urllib.quote(lead_obj.url)
        print "URL: %s" % url
        req = requests.get(url)
        data = req.json()

        if 'status' in data and data['status'] == 'error':
            return None, data.get('message')

        linkedin = data.get('linked_in_response', {})
        events = data.get('change_response', {})
        print "EVENTS: %r" % events 

        if not initial:
            if 'headline' in events:
                headline = events.get('headline')
                detail = 'Old value: %s' % headline.get('old_value')
                lead_obj.events.create(event_type='Headline changed.',
                                       event_detail=detail)
                
        first_name = linkedin.get('firstName', '')
        last_name = linkedin.get('lastName', '')

        lead_obj.name = first_name + ' ' + last_name
        lead_obj.headline = linkedin.get('headline', '')
        lead_obj.image_url = linkedin.get('pictureUrl', '')
        lead_obj.email = linkedin.get('email', '')

        # Add initial "tracking" event
        if initial: 
            lead_obj.events.create(event_type='Now tracking...')

        print "Name: %s" % lead_obj.name
        print "Headline: %s" % lead_obj.headline
        print "Image url: %s" % lead_obj.image_url
        print "Email: %s" % lead_obj.email

        lead_obj.save()
        return lead_obj, ''

    def get_queryset(self):
        utils.is_authed(self.request.user, 'auth.list_leads')
        return Lead.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        # refresh thew list if required
        if kwargs.get('refresh', False):
            leads = self.get_queryset()
            for lead in leads:
                self.update_snitch(lead)

        return super(LeadListView, self).get(request, *args, **kwargs)

    def pre_save(self, obj):
        obj.owner = self.request.user

    def post_save(self, obj, created=False):
        if created:
            obj, msg = self.update_snitch(obj, initial=True)
            if not obj:
                raise Exception(obj)

        return super(LeadListView, self).post_save(obj, created)

class LeadDetailView(generics.RetrieveDestroyAPIView):
    model = Lead
    serializer_class = LeadSerializer
