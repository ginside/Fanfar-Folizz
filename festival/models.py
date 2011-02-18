from django.db import models


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
    ## bug ici	
        return self.groupe.nom + " - " + str(self.heure_passage)
    
# class Programme(models.Model):
#    evenements = models.ForeignKey(Evenement)

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
        return "Informatons Pratiques"
    def __str__(self):
        return "Informatons Pratiques"

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