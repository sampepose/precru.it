from django.conf.urls import patterns, include, url

from dashboard.views import IndexView, LoginView, LogoutView

urlpatterns = patterns('dashboard.views',
    url(r'^$', IndexView.as_view(), name='landing-page'),
    #url(r'^login$', LoginView.as_view(), name='login-view'),
    #url(r'^logout$', LogoutView.as_view(), name='logout-view'),
)
