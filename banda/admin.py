from banda.models import *
from django.contrib import admin


class LienAdmin(admin.ModelAdmin):
    fields = ['adresse','description']

class MediaAdmin(admin.ModelAdmin):
    fields = ['nom','adresse','fichier']

admin.site.register(Lien, LienAdmin)
admin.site.register(Media, MediaAdmin)