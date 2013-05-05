from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.contrib import auth

from rest_framework.response import Response
from rest_framework import generics, parsers, authentication
from rest_framework import exceptions as rest_exceptions

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
        return Lead.objects.filter(owner=self.request.user)

    def pre_save(self, obj):
        obj.owner = self.request.user

    def post_save(self, obj, created=False):
        if created:
            # TODO: Integrate with Dustin's linkedin service
            # URL
            # Oauth token

            obj.name = 'Abe Music'
            obj.email = 'abe.music@gmail.com'
            obj.headline = 'Master of Badassery'
            obj.image_url = 'http://m3.licdn.com/mpr/pub/image-uMMI5Hnk_OUipSn1gv69qpNtt03jl-bjsByisKNWh9tQMsqLGBHYVHNge0tS7htGMK/abe-music.jpg'
            obj.save()

            import random
            for i in range(1, random.randint(2, 6)):
                obj.events.create(event_type='Event type %d' % i)

        return super(LeadListView, self).post_save(obj, created)

