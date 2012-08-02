from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.dates import MONTHS
from django.utils.translation import ugettext_lazy as _

from . import settings
from stripe.widgets import NoNameSelect, NoNameTextInput

class StripePaymentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StripePaymentForm, self).__init__(*args, **kwargs)

    def addError(self, message):
        self._errors[NON_FIELD_ERRORS] = self.error_class([message])
    
    stripe_token = forms.CharField(required=True, widget=forms.HiddenInput())
    
    card_number = forms.CharField(required=False, max_length=20,
        widget=NoNameTextInput())
    
    card_cvc = forms.CharField(
        label=_('Card CVC'),
        help_text=_('Card Verification Code. Last 3 digits on rear of card.'),
        required=False,
        max_length=4,
        widget=NoNameTextInput()
    )
    
    card_expiry_month = forms.ChoiceField(
        label=_('Card expiration month'),
        required=False,
        widget=NoNameSelect(),
        choices=[(m[0], u'%02d - %s' % (m[0], unicode(m[1])))
            for m in sorted(MONTHS.iteritems())]
    )
    
    card_expiry_year = forms.ChoiceField(
        label=_('Card expiration year'),
        required=False,
        widget=NoNameSelect(),
        choices=settings.STRIPE_CARD_YEARS_CHOICES
    )
