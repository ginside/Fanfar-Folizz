__author__ = 'Daniel'

from django.forms import ModelForm
from festival.models import Contact
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
        captcha = CaptchaField()

        class Meta:
            model = Contact
            fields = ['nom', 'prenom', 'mail', 'prestation', 'horaires', 'detail']
