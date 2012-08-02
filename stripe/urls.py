from django.conf.urls.defaults import patterns, url

from stripe import views
from . import settings

urlpatterns = patterns('',
    url(settings.STRIPE_WEBHOOKS_ENDPOINT, views.webhooks, name='webhooks'),
)
