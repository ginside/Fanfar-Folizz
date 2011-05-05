# -*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import date 
from django.shortcuts import render_to_response
from festival.models import Sponsor,Lien,InformationsPratique,Groupe,Festival,Activite,Media

def index(request):
    """page de depart. separation entre les deux sites."""
    
    urlFestival,urlBanda = "/fanfar-folizz","/banda-tchitchaa"
    retour = {
		'date' : date.today(),
		'urlFestival' : urlFestival,
		'urlBanda' : urlBanda
	}
    return render_to_response('index.html',retour)


def	accueil(request):
	"""page d'accueil du site du festival."""
	specific_stylesheet = "Accueil.css"
	titre_page = "Accueil"
	
	retour = {
		'titre' : titre_page,
		'specific_stylesheet' : specific_stylesheet
	}
	return render_to_response('festival/accueil.html',retour)
	
def sponsors(request):
	"""sponsors du festival."""
	retour = {
		'titre'    : "Partenaires",
		'sponsors' : Sponsor.objects.all(),
	}
	
	return render_to_response('festival/accueil_sponsors.html',retour)
	
def liens(request):
	"""liens divers."""
	retour = {
		'titre' : "Liens",
		'liens' : Lien.objects.all(),
	}
	
	return render_to_response('festival/accueil_liens.html',retour)
	
def infos(request):
	"""infos pratiques."""
	retour = {
		'titre' : u"Informations Pratiques",
		'infos' : InformationsPratique.objects.all(),
	}
	
	return render_to_response('festival/accueil_infos.html',retour)
	
def groupes(request):
	"""liste des groupes en base."""
	retour = {
		'titre' : u"Les groupes",
		'groupes' : Groupe.objects.all(),
	}
	
	return render_to_response('festival/accueil_groupes.html',retour)
	
def groupe_detail(request, groupe_id):
	""" detail d un groupe"""
	groupe = Groupe.objects.get(id= groupe_id )
	retour = {
		'titre' : groupe.nom,
		'groupe' : groupe,
	}
	return render_to_response('festival/accueil_detail_groupe.html',retour)
	
def programme(request):
	""" programme du festival le plus recent en base) """
	festival = Festival.objects.latest(field_name="date_creation")
	dates = []
	for evenement in festival.evenements.all():
		dates.append(evenement.heure_passage.date())
	liste_dates = []
	for date in set(dates):
		liste_dates.append(date)
	liste_dates.sort()
	
	retour = {
		'titre' : festival.nom,
		'festival' : festival,
		'dates' : liste_dates,
	}
	return render_to_response('festival/accueil_programme.html',retour)
	
def medias(request):
	""" vidéos, images et pdfs """
	medias = Media.objects.order_by('festival')
	
	for media in medias:
		if len(media.adresse):
			if media.adresse.find('youtube') != -1:
				src = "http://www.youtube.com/embed/"+ media.adresse[media.adresse.find("?v=")+3:]
			elif media.adresse.find('youtu.be') != -1:
				src = "http://www.youtube.com/embed/"+ media.adresse[16:]
			elif media.adresse.find('dailymotion') != -1:
				video_id = ''
				
				
			media.code = u'<iframe width="380" height="285" src="'+ src +u'" frameborder="0" allowfullscreen></iframe>'
				
	retour = {
		'medias' : medias,
	}
	return render_to_response('festival/accueil_medias.html',retour)