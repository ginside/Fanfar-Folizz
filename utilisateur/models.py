from django.db import models

# Create your models here.

class User(models.Model):
	login = models.CharField(max_length=32,unique=True)
	mot_de_passe = models.CharField(max_length=32)
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	ROLE_CHOICES = (
		('admin', 'administrateur'),
		('webmaster', 'webmestre'),
		('user', 'utilisateur')
	)
	email = models.EmailField()
	role = models.CharField(max_length=32, choices=ROLE_CHOICES)
	
	def __unicode__(self):
		return self.login + " (" + self.prenom + " " + self.nom + ")"
	def __str__(self):
		return self.login + " (" + self.prenom + " " + self.nom + ")"
