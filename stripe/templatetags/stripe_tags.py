from django import template

from .. import settings

register = template.Library()

@register.inclusion_tag('stripe/stripe_head.html', takes_context=True)
def stripe_head(context):
    context["STRIPE_PUBLISHABLE_KEY"] = settings.STRIPE_PUBLISHABLE_KEY
    return context

@register.inclusion_tag('stripe/stripe_card_form.html', takes_context=True)
def stripe_card_form(context):
    return context
