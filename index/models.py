from django.db import models
from utilisateur.models import User
# Create your models here.

class General(models.Model):
    utilisateur = models.ForeignKey(User)
    contact = models.EmailField()
    
    def __unicode__(self):
	return "infos generales"