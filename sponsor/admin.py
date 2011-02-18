from sponsor.models import Sponsor
from django.contrib import admin

class SponsorAdmin(admin.ModelAdmin):
	fields = ['nom','logo','description']

admin.site.register(Sponsor, SponsorAdmin)
