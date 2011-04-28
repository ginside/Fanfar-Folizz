from django.http import HttpResponse
from datetime import date 
from django.shortcuts import render_to_response
from festival.models import Sponsor,Lien,InformationsPratique,Groupe


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