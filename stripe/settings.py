import datetime

from django.conf import settings as _settings

_today = datetime.date.today()

_audit_defaults = {
    'active': 'active',
    'trialing': 'trialing',
    'past_due': 'past_due',
    'suspended': 'suspended',
    'unpaid': 'unpaid',
    'cancelled': 'cancelled',
    'no_subscription': 'no_subscription',
}

STRIPE_PUBLISHABLE_KEY = getattr(_settings, 'STRIPE_PUBLISHABLE_KEY')

STRIPE_SECRET_KEY = getattr(_settings, 'STRIPE_SECRET_KEY')

STRIPE_WEBHOOKS_ENDPOINT = getattr(_settings, 'STRIPE_WEBHOOKS_ENDPOINT',
    r'webhooks/$')

STRIPE_CARD_YEARS = getattr(_settings, 'STRIPE_CARD_YEARS',
    range(_today.year, _today.year + 10))

STRIPE_CARD_YEARS_CHOICES = getattr(_settings, 'STRIPE_CARD_YEARS_CHOICES',
    [(i,i) for i in STRIPE_CARD_YEARS])

STRIPE_MAXIMUM_CUSTOMER_LIST_SIZE = getattr(_settings,
    'STRIPE_MAXIMUM_CUSTOMER_LIST_SIZE', 100)

STRIPE_AUDIT_RESULTS = getattr(_settings, 'STRIPE_AUDIT_RESULTS', _audit_defaults)

STRIPE_ACTIVE_STATUSES = getattr(_settings, 'STRIPE_ACTIVE_STATUSES',
    ('active', 'trialing', 'past_due'))

STRIPE_INACTIVE_STATUSES = getattr(_settings, 'STRIPE_INACTIVE_STATUSES',
    ('suspended', 'unpaid', 'cancelled', 'no_subscription'))
