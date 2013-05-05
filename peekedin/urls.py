import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin URL
    url(r'^_foo/admin/', include(admin.site.urls)),

    # Dashboard
    url(r'', include('dashboard.urls')),
)

# Remove this comment and indent the following few lines
# when we're in production. This is to get Heroku to
# serve up static files properly.
if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
