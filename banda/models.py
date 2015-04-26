
from django.db import models
from festival.models import Contact
from django.contrib.auth import get_user_model


class Article(models.Model):
    titre = models.CharField(max_length = 64)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now = True)
    auteur = models.ForeignKey(get_user_model(), related_name='auteur_banda')
    
    def __str__(self):
        return self.titre[:15]+'..' if len(self.titre) > 15 else self.titre

TYPE_MEDIA = (
    ('p', 'Photo'),
    ('v', 'Vidéo'),
    ('j', 'Journal'),
)
class Media(models.Model):
    nom = models.CharField(max_length = 50)
    adresse = models.URLField(blank = True)
    fichier = models.FileField(upload_to = "files/",blank = True)
    
    def image_tag(self):
        if self.adresse or self.fichier.name[-3:] == "pdf" :
            return '<a href="self' + self.adresse + '">'+self.adresse+'</a>'
        return u'<img src="%s" style="max-width:320px"/>' % self.fichier.url
        return ""
    image_tag.short_description = 'Aperçu'
    image_tag.allow_tags = True
    
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
        try:        
            if len(self.fichier):
                extension = str(self.fichier).split(".")[-1]
                # le média est une image
                if extension in ['jpg','png','jpeg','gif','bmp']:
                    self.type = "image"
                    
                # le média est un pdf
                elif extension == 'pdf':
                    self.type = extension
        except FileNotFoundError:
            return False
        return True

class Lien(models.Model):
    adresse = models.URLField()
    description = models.CharField(max_length = 200,blank = True)
    def __str__(self):
        return self.adresse

TYPE_MEMBRE = (
    ('f', 'Fixe'),
    ('p', 'Ponctuel'),
    ('t', 'Temporaire'),
)
class Membre(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/membres', blank=True)
    instrument = models.CharField(max_length=50)
    blabla = models.TextField(blank=True)
    type = models.CharField(choices=TYPE_MEMBRE, max_length=1)
    afficher = models.BooleanField()

    def __str__(self):
        return str(self.type.upper() + ' - ' + self.prenom + ' ' + self.nom + '(' + self.instrument + ')')

class DateEvenement(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length = 200,blank = True)
    date = models.DateTimeField()

class Music(models.Model):
    titre = models.CharField(max_length=50)
    lien = models.URLField()
    partoche = models.FileField(upload_to = "files/partoches",blank = True)

class BandaContact(Contact):
    class Meta:
        proxy = True