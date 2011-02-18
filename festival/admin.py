from festival.models import Groupe,Evenement,Sponsor,InformationsPratique,Historique,Lien
from django.contrib import admin

class GroupeAdmin(admin.ModelAdmin):
	fields = ['nom','style','origine','photo','description']
	
class EvenementAdmin(admin.ModelAdmin):
	fields = ['groupe','lieu','heure_passage']
	
# class ProgrammeAdmin(admin.ModelAdmin):
#	fields = ['evenements']
	
class SponsorAdmin(admin.ModelAdmin):
	fields = ['nom','logo','description']
	
class InformationsPratiqueAdmin(admin.ModelAdmin):
	fields = ['carte','explications','autresInformations']
	
class HistoriqueAdmin(admin.ModelAdmin):
	fields = ['dates','description']
	
class LienAdmin(admin.ModelAdmin):
	fields = ['adresse','description']
	
admin.site.register(Groupe, GroupeAdmin)
admin.site.register(Evenement, EvenementAdmin)
admin.site.register(InformationsPratique, InformationsPratiqueAdmin)
admin.site.register(Historique, HistoriqueAdmin)
admin.site.register(Lien, LienAdmin)
admin.site.register(Sponsor, SponsorAdmin)
