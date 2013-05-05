import settings
from django.conf.urls import patterns, include, url

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

##
# API Index
##

@api_view(['GET'])
@authentication_classes((SessionAuthentication,))
def api_root(request, format=None):
    return Response({
        'core':  {
            'ping': reverse('ping-view', request=request, format=format),
            'register': reverse('register-view', request=request, format=format),
            'login': reverse('login-view', request=request, format=format),
            'logout': reverse('logout-view', request=request, format=format),
        },
        'leads': reverse('lead-list-view', request=request, format=format),
    })

urlpatterns = patterns('',
    # API stuff
    url(r'^api/$', api_root),
    url(r'^api/', include('core.urls')),
    url(r'^api/leads/', include('leads.urls')),
 
    # Admin URL
    url(r'^_foo/admin/', include(admin.site.urls)),

    # linked in auth
    url(r'^linkedin/login$', 'core.views.linkedin_login'),
    url(r'^linkedin/logout$', 'core.views.linkedin_logout'),
    url(r'^linkedin/authenticated$', 'core.views.linkedin_authenticated'),

    # Dashboard
    url(r'', include('dashboard.urls')),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
