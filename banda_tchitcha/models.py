# -*- coding: utf-8 -*-

from django.db import models

TYPE_MEMBRE = (
	('f', 'Fixe'),
	('p', 'Ponctuel'),
	('t', 'Temporaire'),
)
TYPE_MEDIA = (
	('p', 'Photo'),
	('v', 'Vidéo'),
	('j', 'Journal'),
)

class News(models.model):
	titre = models.CharField(max_length = 50)
	texte = models.TextField()
	date = models.DateTimeField(auto_now_add = True, blank = True)

class Membre(models.model):
	nom = models.CharField(max_length = 50)
	photo = models.ImageField(upload_to = "membres", blank = True)
	instrument = models.CharField(max_length = 50)
	blabla = models.TextField(blank = True)
	type = models.CharField(choices = TYPE_MEMBRE, max_length = 1)
	
	def __str__(self):
		return str(self.nom + self.instrument)
		
	def __unicode__(self):
		return unicode(self.nom + self.instrument)
		
class Media(models.Model):
	nom = models.CharField(max_length = 50)
	adresse = models.URLField(blank = True)
	fichier = models.FileField(upload_to = "files/",blank = True)
	type = models.CharField(max_length = 1, choices = TYPE_MEDIA)
	
	def __unicode__(self):
		return unicode(self.nom) + " - "+ unicode(self.type)
	
	def __str__(self):
		return str(self.nom) + " - "+ str(self.type)
	
class Lien(models.Model):
    adresse = models.URLField()
    description = models.CharField(max_length = 200,blank = "true")
    
    def __unicode__(self):
        return self.adresse
    def __str__(self):
        return self.adresse