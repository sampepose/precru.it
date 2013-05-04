from django.conf.urls import patterns, include, url

from dashboard.views import IndexView

urlpatterns = patterns('dashboard.views',
    url(r'^$', IndexView.as_view()),
)
