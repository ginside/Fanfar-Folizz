from django.contrib import admin
from index.models import General

class GeneralAdmin(admin.ModelAdmin):
    fields = ['utilisateur','contact']
    
admin.site.register(General,GeneralAdmin)
