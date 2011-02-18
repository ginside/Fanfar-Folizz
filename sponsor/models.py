from django.db import models


class Sponsor(models.Model):
    nom = models.CharField(max_length = 50)
    logo = models.ImageField(upload_to="images")
    description = models.CharField(max_length = 50)

    def __unicode__(self):
	return self.nom

    def __str__(self):
	return self.nom