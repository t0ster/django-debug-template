from django.conf.urls.defaults import *

from example.views import MyView


urlpatterns = patterns('',
    (r'^$', MyView.as_view()),
)
