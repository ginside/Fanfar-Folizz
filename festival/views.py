# -*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import date 
from django.shortcuts import render_to_response
from festival.models import Sponsor,Lien,InformationsPratique,Groupe,Festival,Activite,Media,Article
from django.conf import settings 
from django.template.context import RequestContext
from django.core.urlresolvers import reverse

def index(request):
    """page de depart. separation entre les deux sites."""
    return render_to_response('index.html',RequestContext(request))


def accueil(request):
    """page d'accueil du site du festival."""
    articles = Article.objects.all().order_by('date')[:10]
    retour = {
        'news' : Article.objects.all().order_by('date')[:10]
    }
    return render_to_response('festival/accueil.html',RequestContext(request, retour))
    
def sponsors(request):
    """sponsors du festival."""
    retour = {
        'sponsors' : Sponsor.objects.all(),
    }
    return render_to_response('festival/sponsors.html',RequestContext(request, retour))
    
def liens(request):
    """liens divers."""
    retour = {
        'liens' : Lien.objects.all(),
    }
    return render_to_response('festival/liens.html',RequestContext(request, retour))
    
def infos(request):
    """infos pratiques."""
    retour = {
        'infos' : InformationsPratique.objects.all(),
    }
    
    return render_to_response('festival/infos_pratiques.html',RequestContext(request, retour))
    
def groupes(request):
    """liste des groupes en base."""
    retour = {
        'groupes' : Groupe.objects.all(),
    }
    
    return render_to_response('festival/groupe_list.html',RequestContext(request, retour))
    
def groupe_detail(request, groupe_id):
    """ detail d un groupe"""
    groupe = Groupe.objects.get(id= groupe_id )
    retour = {
        'groupe' : groupe,
    }
    return render_to_response('festival/groupe_detail.html',RequestContext(request, retour))
    
def programme(request):
    """ programme du festival le plus recent en base) """
    try:
        festival = Festival.objects.latest(field_name="date_creation")
    except:
        return render_to_response('festival/accueil.html')
    liste_dates, dates = ([] for i in range(2))
    for evenement in festival.evenements.all():
        dates.append(evenement.heure_passage.date())
    for date in set(dates):
        liste_dates.append(date)
    liste_dates.sort()
    
    retour = {
        'festival' : festival,
        'dates' : liste_dates,
    }
    return render_to_response('festival/programme.html',RequestContext(request, retour))
    
def medias(request):
    """ vidéos, images et pdfs """
    medias = Media.objects.all()
    try:
        #debile
       dernier_festival = Festival.objects.get(nom__endswith = '2013')
    except:
        return render_to_response('festival/accueil.html', RequestContext(request, {}))
        
    for media in medias:
        media.display()

    retour = {
        'medias' : medias,
        'def' : dernier_festival.id,
    }
    return render_to_response('festival/medias.html',RequestContext(request, retour))
    
def historique(request):
    """historique des précédentes éditions, médias"""
    anciens_festivals = Festival.objects.filter(historise = 1)
    anciens_ids_festival = []
    for f in anciens_festivals:
        anciens_ids_festival.append(f.id)
    historique,retour = 0,{}
    if len(anciens_festivals):
        historique = 1
        medias = Media.objects.all()
        for media in medias:
            if isinstance(media.festival,Festival):
                if media.festival.id in anciens_ids_festival:
                    # le média est une vidéo
                    if len(media.adresse):
                        media.type = "video"
                        if media.adresse.find('youtube') != -1:
                            src = "http://www.youtube.com/embed/"+ media.adresse[media.adresse.find("?v=")+3:]
                        elif media.adresse.find('youtu.be') != -1:
                            src = "http://www.youtube.com/embed/"+ media.adresse[16:]
                        elif media.adresse.find('dailymotion') != -1:
                            src = 'http://www.dailymotion.com/embed/video/'+ media.adresse.split("/video/")[1].split("_")[0] +'?theme=none&wmode=transparent'
                        else:
                            media.code = media.adresse
                            continue
                        media.code = u'<iframe width="380" height="285" src="'+ src +u'" frameborder="0" allowfullscreen></iframe>'
                    
                    elif len(media.fichier):
                        extension = str(media.fichier).split(".")[-1]
                        # le média est une image
                        if extension in ['jpg','png','jpeg','gif','bmp']:
                            media.type ="image"
                            
                        # le média est un pdf
                        elif extension == 'pdf':
                            media.type = extension
            retour = {
                'medias' : medias,
                'historique' : historique,
                }
    return render_to_response('festival/historique.html',RequestContext(request, retour))

def news(request):
    retour = {
        'news' : Article.objects.all().order_by('date')[:10]
    }
    return render_to_response('festival/_news.html',RequestContext(request, retour))
