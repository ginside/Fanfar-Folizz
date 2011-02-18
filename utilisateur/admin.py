from utilisateur.models import User
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
	fields = ['login','mot_de_passe','nom','prenom','email','role']

admin.site.register(User, UserAdmin)
