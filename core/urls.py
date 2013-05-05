from django.conf.urls.defaults import *
from .api import *

urlpatterns = patterns('core.api',
    url(r'^ping/$',
        PingView.as_view(), 
        name='ping-view'),

    url(r'^register/$',
        RegisterView.as_view(), 
        name='register-view'),

    url(r'^login/$',
        LoginView.as_view(), 
        name='login-view'),

    url(r'^logout/$',
        LogoutView.as_view(), 
        name='logout-view'),
)


