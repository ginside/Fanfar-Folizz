from festival.models import *
from django.contrib import admin

class GroupeAdmin(admin.ModelAdmin):
    fields = ['nom','style','origine','photo','description']
    
class EvenementAdmin(admin.ModelAdmin):
    fields = ['groupe','lieu','heure_passage']
    
class ActiviteAdmin(admin.ModelAdmin):
    fields = ['qui','quoi','lieu','photo','date','autres_informations']

class FestivalAdmin(admin.ModelAdmin):
    fields = ['nom','evenements','activites','historise']
    
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
    
class ArticleAdmin(admin.ModelAdmin):
    fields = ['titre','contenu']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance,'auteur'):
            instance.auteur = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change): 
        def set_user(instance):
            if not instance.auteur:
                instance.auteur = request.user
            instance.save()
        if formset.model == Article:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()
    
admin.site.register(Groupe, GroupeAdmin)
admin.site.register(Evenement, EvenementAdmin)
admin.site.register(InformationsPratique, InformationsPratiqueAdmin)
admin.site.register(Historique, HistoriqueAdmin)
admin.site.register(Lien, LienAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Activite, ActiviteAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Article, ArticleAdmin)