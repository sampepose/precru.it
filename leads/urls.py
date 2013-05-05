from django.conf.urls.defaults import *
from .api import LeadListView

urlpatterns = patterns('leads.api',
    url(r'^$',
        LeadListView.as_view(), 
        name='lead-list-view'),
)
