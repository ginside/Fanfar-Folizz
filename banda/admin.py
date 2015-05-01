from banda.models import *
from django.contrib import admin


class LienAdmin(admin.ModelAdmin):
    fields = ['adresse','description']

class MediaAdmin(admin.ModelAdmin):
    fields = ['nom','adresse','fichier','image_tag']
    readonly_fields = ('image_tag',)
    list_display = ('nom', 'image_tag')

class MembreAdmin(admin.ModelAdmin):
    fields = ['nom','prenom','photo','instrument','blabla','type','afficher']
    
class MusicAdmin(admin.ModelAdmin):
    fields = ['titre','lien','partoche']
    
class ArticleAdmin(admin.ModelAdmin):
    fields = ['titre','contenu']
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.auteur = request.user
        instance.save()
        form.save_m2m()
        return instance
    
admin.site.register(Lien, LienAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Membre, MembreAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Article, ArticleAdmin)