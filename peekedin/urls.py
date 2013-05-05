import settings
from django.conf.urls import patterns, include, url

from rest_framework.decorators import api_view
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
def api_root(request, format=None):
    return Response({
        'core':  {
            'ping': reverse('ping-view', request=request, format=format),
            'register': reverse('register-view', request=request, format=format),
            'login': reverse('login-view', request=request, format=format),
            'logout': reverse('logout-view', request=request, format=format),
        },
        'leads': {
        },
    })

urlpatterns = patterns('',
    # API stuff
    (r'^api/$', api_root),
    url(r'^api/', include('core.urls')),
    
    # Admin URL
    url(r'^_foo/admin/', include(admin.site.urls)),

    # Dashboard
    url(r'', include('dashboard.urls')),
)

#urlpatterns += patterns('',
#    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

