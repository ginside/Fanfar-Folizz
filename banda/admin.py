from banda.models import *
from django.contrib import admin


class LienAdmin(admin.ModelAdmin):
    fields = ['adresse','description']

class MediaAdmin(admin.ModelAdmin):
    fields = ['nom','adresse','fichier']

class MembreAdmin(admin.ModelAdmin):
    fields = ['nom','prenom','photo','instrument','blabla','type','afficher']
    
class MusicAdmin(admin.ModelAdmin):
    fields = ['titre','lien','partoche']

admin.site.register(Lien, LienAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Membre, MembreAdmin)
admin.site.register(Music, MusicAdmin)