import logging

from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

import stripe
from . import settings
from stripe.signals import StripeWebhook, WEBHOOK_MAP

log = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def webhooks(request):
    """
    Handles all known webhooks from stripe, and calls signals.
    Plug in as you need.
    """
    if request.method != "POST":
        return HttpResponse(status=405)

    try:
        event_json = simplejson.loads(request.raw_post_data)
    except ValueError:
        return HttpResponse(status=400)
    
    event_key = event_json['type'].replace('.', '_')

    if event_key in WEBHOOK_MAP:
        log.info('Received Stripe webhook call for event %s' % event_key)
        WEBHOOK_MAP[event_key].send_robust(sender=StripeWebhook, full_json=event_json)

    return HttpResponse(status=200)
