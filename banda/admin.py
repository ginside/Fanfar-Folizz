from banda.models import *
from django.contrib import admin


class LienAdmin(admin.ModelAdmin):
    fields = ['adresse','description']

class MediaAdmin(admin.ModelAdmin):
    fields = ['nom','adresse','fichier']

class MembreAdmin(admin.ModelAdmin):
    fields = ['nom','prenom','photo','instrument','blabla','type','afficher']
    
admin.site.register(Lien, LienAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Membre, MembreAdmin)