from django.db import models
from django.utils.encoding import force_unicode

class Groupe(models.Model):
    nom = models.CharField(max_length = 50)
    style = models.CharField(max_length = 50)
    origine = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to = "images")
    description = models.TextField()
    
    def __unicode__(self):
        return self.nom + unicode(" ( ") + self.origine + unicode(" )")
    def __str__(self):
        return self.nom + str(" ( ") + self.origine + str(" )")

		
class Evenement(models.Model):
    groupe = models.ForeignKey(Groupe)
    lieu = models.CharField(max_length = 50)
    heure_passage = models.DateTimeField()
    def __unicode__(self):
        return self.groupe.nom + " - " + str(self.heure_passage)
    


class Activite(models.Model):
	qui = models.CharField(max_length = 50)
	quoi = models.TextField()
	lieu = models.CharField(max_length = 50)
	date = models.DateTimeField()
	autres_informations = models.TextField()
	
	def __unicode__(self):
		sujet = unicode(self.quoi)
		if len(sujet) > 50:
			sujet = sujet[:50]+u"..."
		return self.qui + " - " +  sujet + u" [heure " + unicode(self.date.time())[:5] + " - date " + unicode(self.date.date()) + u"]"
	
class Festival(models.Model):
	nom = models.CharField(max_length = 50)
	evenements = models.ManyToManyField(Evenement)
	activites = models.ManyToManyField(Activite, blank = True)
	date_creation = models.DateTimeField(auto_now_add = True, blank = True)
	historise = models.BooleanField()
	
	def __unicode__(self):
		return self.nom

class Media(models.Model):
	nom = models.CharField(max_length = 50)
	adresse = models.URLField(blank = True)
	fichier = models.FileField(upload_to = "files/",blank = "True")
	festival = models.ForeignKey('Festival', blank = "True", null = "True")
	
	def __unicode(self):
		return self.festival + unicode(" - ") + force_unicode(self.nom)
	
	def __str__(self):
		festival = "Aucun festival"
		if not str(self.festival) == "None":
			festival = str(self.festival)
		return  festival + " - " + self.nom
		
class Sponsor(models.Model):
    nom = models.CharField(max_length = 50)
    logo = models.ImageField(upload_to="images")
    description = models.CharField(max_length = 50,blank = "true")

    def __unicode__(self):
        return self.nom

    def __str__(self):
        return self.nom

		
class InformationsPratique(models.Model):
    carte = models.ImageField(upload_to = "images")
    explications = models.TextField()
    autresInformations = models.TextField()
    def __unicode__(self):
        return "Informations Pratiques"
    def __str__(self):
        return "Informations Pratiques"

		
class Historique(models.Model):
    description = models.TextField()
    dates = models.DateTimeField()

    def __unicode__(self):
        return "Edition" + self.dates
    def __str__(self):
        return "Edition" + self.dates


class Lien(models.Model):
    adresse = models.URLField()
    description = models.CharField(max_length = 200,blank = "true")
    
    def __unicode__(self):
        return self.adresse
    def __str__(self):
        return self.adresse