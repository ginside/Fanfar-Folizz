__author__ = 'Daniel'

from django.forms import ModelForm
from banda.models import BandaContact
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
        captcha = CaptchaField()

        class Meta:
            model = BandaContact
            fields = ['nom', 'prenom', 'mail', 'prestation', 'horaires', 'detail']
