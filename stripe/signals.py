"""
Provides the following signals:

- stripe_webhook_charge_succeeded
- stripe_webhook_charge_failed
- stripe_webhook_charge_refunded
- stripe_webhook_charge_disputed
- stripe_webhook_customer_created
- stripe_webhook_customer_updated
- stripe_webhook_customer_deleted
- stripe_webhook_customer_subscription_created
- stripe_webhook_customer_subscription_updated
- stripe_webhook_customer_subscription_deleted
- stripe_webhook_customer_subscription_trial_will_end
- stripe_webhook_customer_discount_created
- stripe_webhook_customer_discount_updated
- stripe_webhook_customer_discount_deleted
- stripe_webhook_invoice_created
- stripe_webhook_invoice_updated
- stripe_webhook_invoice_payment_succeeded
- stripe_webhook_invoice_payment_failed
- stripe_webhook_invoiceitem_created
- stripe_webhook_invoiceitem_updated
- stripe_webhook_invoiceitem_deleted
- stripe_webhook_plan_created
- stripe_webhook_plan_updated
- stripe_webhook_plan_deleted
- stripe_webhook_coupon_created
- stripe_webhook_coupon_updated
- stripe_webhook_coupon_deleted
- stripe_webhook_transfer_created
- stripe_webhook_transfer_failed
- stripe_webhook_ping
"""

import django.dispatch

class StripeWebhook(object):
    pass

WEBHOOK_ARGS = ["full_json"]

stripe_webhook_charge_succeeded = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_charge_failed = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_charge_refunded = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_charge_disputed = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_customer_created = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_customer_updated = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_customer_deleted = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_customer_subscription_created = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_customer_subscription_updated = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_customer_subscription_deleted = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_customer_subscription_trial_will_end = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_customer_discount_created = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_customer_discount_updated = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_customer_discount_deleted = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_invoice_created = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_invoice_updated = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_invoice_payment_succeeded = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_invoice_payment_failed = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_invoiceitem_created = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_invoiceitem_updated = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_invoiceitem_deleted = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_plan_created = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_plan_updated = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_plan_deleted = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_coupon_created = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_coupon_updated = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_coupon_deleted = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_transfer_created = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_transfer_failed = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
stripe_webhook_ping = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)

WEBHOOK_MAP = {
    'charge_succeeded': stripe_webhook_charge_succeeded,
    'charge_failed': stripe_webhook_charge_failed,
    'charge_refunded': stripe_webhook_charge_refunded,
    'charge_disputed': stripe_webhook_charge_disputed,
    'customer_created': stripe_webhook_customer_created,
    'customer_updated': stripe_webhook_customer_updated,
    'customer_deleted': stripe_webhook_customer_deleted,
    'customer_subscription_created': stripe_webhook_customer_subscription_created,
    'customer_subscription_updated': stripe_webhook_customer_subscription_updated,
    'customer_subscription_deleted': stripe_webhook_customer_subscription_deleted,
    'customer_subscription_trial_will_end': stripe_webhook_customer_subscription_trial_will_end,
    'customer_discount_created': stripe_webhook_customer_discount_created,
    'customer_discount_updated': stripe_webhook_customer_discount_updated,
    'customer_discount_deleted': stripe_webhook_customer_discount_deleted,
    'invoice_created': stripe_webhook_invoice_created,
    'invoice_updated': stripe_webhook_invoice_updated,
    'invoice_payment_succeeded': stripe_webhook_invoice_payment_succeeded,
    'invoice_payment_failed': stripe_webhook_invoice_payment_failed,
    'invoiceitem_created': stripe_webhook_invoiceitem_created,
    'invoiceitem_updated': stripe_webhook_invoiceitem_updated,
    'invoiceitem_deleted': stripe_webhook_invoiceitem_deleted,
    'plan_created': stripe_webhook_plan_created,
    'plan_updated': stripe_webhook_plan_updated,
    'plan_deleted': stripe_webhook_plan_deleted,
    'coupon_created': stripe_webhook_coupon_created,
    'coupon_updated': stripe_webhook_coupon_updated,
    'coupon_deleted': stripe_webhook_coupon_deleted,
    'transfer_created': stripe_webhook_transfer_created,
    'transfer_failed': stripe_webhook_transfer_failed,
    'ping': stripe_webhook_ping,
}
