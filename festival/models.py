# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model

class Groupe(models.Model):
    nom = models.CharField(max_length = 50)
    style = models.CharField(max_length = 50)
    origine = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to = "images")
    description = models.TextField()
    
    def __unicode__(self):
        return self.nom + " ( " + self.origine + " )"
    def __str__(self):
        return self.nom + str(" ( ") + self.origine + str(" )")

        
class Evenement(models.Model):
    groupe = models.ForeignKey(Groupe)
    lieu = models.CharField(max_length = 50)
    heure_passage = models.DateTimeField()
    def __str__(self):
        return self.groupe.nom + " - " + str(self.heure_passage)

class Activite(models.Model):
    qui = models.CharField(max_length = 50)
    quoi = models.TextField()
    lieu = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to = "images", blank = True)
    date = models.DateTimeField()
    autres_informations = models.TextField()
    def __str__(self):
        return self.qui + " - " + self.quoi + str(self.date)

class Festival(models.Model):
    nom = models.CharField(max_length = 50)
    evenements = models.ManyToManyField(Evenement)
    activites = models.ManyToManyField(Activite, blank = True)
    date_creation = models.DateTimeField(auto_now_add = True, blank = True)
    historise = models.BooleanField()
    def __str__(self):
        return self.nom

class Media(models.Model):
    nom = models.CharField(max_length = 50)
    adresse = models.URLField(blank = True)
    fichier = models.FileField(upload_to = "files/",blank = True)
    festival = models.ForeignKey('Festival', blank = True, null = True)
    
    def __str__(self):
        festival = "Aucun festival"
        if not str(self.festival) == "None":
            festival = str(self.festival)
        return  festival + " - " + self.nom

    def display(self):
        # if isinstance(media.festival,Festival):
        #     if media.festival.id == dernier_festival.id:
        # le média est une vidéo
        if len(self.adresse):
            self.type = "video"
            src = None
            if self.adresse.find('youtube') != -1:
                src = "http://www.youtube.com/embed/"+ self.adresse[self.adresse.find("?v=")+3:]
            elif self.adresse.find('youtu.be') != -1:
                src = "http://www.youtube.com/embed/"+ self.adresse[16:]
            elif self.adresse.find('dailymotion') != -1:
                src = 'http://www.dailymotion.com/embed/video/'+ self.adresse.split("/video/")[1].split("_")[0] +'?theme=none&wmode=transparent'
            else:
                self.code = self.adresse
            if src:    #width="380" height="285"
                self.code = '<iframe class="col-lg-12 col-md-12 col-sm-12 col-xs-12 video_frame" style="height:250px" src="'+ src +'"     frameborder="0" allowfullscreen></iframe>'
        
        elif len(self.fichier):
            extension = str(self.fichier).split(".")[-1]
            # le média est une image
            if extension in ['jpg','png','jpeg','gif','bmp']:
                self.type = "image"
                
            # le média est un pdf
            elif extension == 'pdf':
                self.type = extension
    
class Sponsor(models.Model):
    nom = models.CharField(max_length = 50)
    logo = models.ImageField(upload_to="images")
    description = models.CharField(max_length = 50,blank = True)

    def __str__(self):
        return self.nom

        
class InformationsPratique(models.Model):
    carte = models.ImageField(upload_to = "images")
    explications = models.TextField()
    autresInformations = models.TextField()
    def __str__(self):
        return "Informations Pratiques"

        
class Historique(models.Model):
    description = models.TextField()
    dates = models.DateTimeField()

    def __str__(self):
        return "Edition" + self.dates


class Lien(models.Model):
    adresse = models.URLField()
    description = models.CharField(max_length = 200,blank = True)
    
    def __str__(self):
        return self.adresse
    
class Article(models.Model):
    titre = models.CharField(max_length = 64)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now = True)
    auteur = models.ForeignKey(get_user_model())
    
    def __str__(self):
        return self.titre[:15]+'..' if len(self.titre) > 15 else self.titre