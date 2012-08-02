from . import settings

AUDIT_RESULTS = settings.STRIPE_AUDIT_RESULTS
ACTIVE_STATUSES = settings.STRIPE_ACTIVE_STATUSES
INACTIVE_STATUSES = settings.STRIPE_INACTIVE_STATUSES

def audit_customer_subscription(customer):
    """
    Audits the provided customer's subscription against stripe and returns a pair
    that contains a boolean and a result type.

    Default result types can be found in stripe.settings.defaults and can be
    overridden in your project's settings.
    """
    if (hasattr(customer, 'suspended') and customer.suspended):
        active = 'suspended' in ACTIVE_STATUSES
        result = AUDIT_RESULTS['suspended']
    
    else:
        if hasattr(customer, 'subscription'):
            try:
                status = customer.subscription.status
                active = status in ACTIVE_STATUSES
                result = AUDIT_RESULTS[status]
            except KeyError, err:
                raise Exception("Unable to locate a result set for subscription status %s in STRIPE_AUDIT_RESULTS") % str(err)
        else:
            active = 'no_subscription' in ACTIVE_STATUSES
            result = AUDIT_RESULTS['no_subscription']
    return {'active': active, 'result': result}