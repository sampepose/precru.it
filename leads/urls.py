from django.conf.urls.defaults import *
from .api import LeadListView, LeadDetailView

urlpatterns = patterns('leads.api',
    url(r'^$',
        LeadListView.as_view(), 
        name='lead-list-view'),

    url(r'^(?P<pk>[0-9]+)/$', 
        LeadDetailView.as_view(), 
        name='lead-detail-view'),
)
