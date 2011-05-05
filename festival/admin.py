from models import Groupe,Evenement,Sponsor,InformationsPratique,Historique,Lien,Activite,Festival,Media
from django.contrib import admin

class GroupeAdmin(admin.ModelAdmin):
	fields = ['nom','style','origine','photo','description']
	
class EvenementAdmin(admin.ModelAdmin):
	fields = ['groupe','lieu','heure_passage']
	
class ActiviteAdmin(admin.ModelAdmin):
	fields = ['qui','quoi','lieu','date','autres_informations']

class FestivalAdmin(admin.ModelAdmin):
	fields = ['nom','evenements','activites']
	
class SponsorAdmin(admin.ModelAdmin):
	fields = ['nom','logo','description']
	
class InformationsPratiqueAdmin(admin.ModelAdmin):
	fields = ['carte','explications','autresInformations']
	
class HistoriqueAdmin(admin.ModelAdmin):
	fields = ['dates','description']
	
class LienAdmin(admin.ModelAdmin):
	fields = ['adresse','description']

class MediaAdmin(admin.ModelAdmin):
	fields = ['nom','adresse','fichier','festival']
	
admin.site.register(Groupe, GroupeAdmin)
admin.site.register(Evenement, EvenementAdmin)
admin.site.register(InformationsPratique, InformationsPratiqueAdmin)
admin.site.register(Historique, HistoriqueAdmin)
admin.site.register(Lien, LienAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Activite, ActiviteAdmin)
admin.site.register(Media, MediaAdmin)