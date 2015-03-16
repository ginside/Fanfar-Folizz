# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from banda.models import Lien, Article, Media, Membre, Music
from banda.forms import ContactForm
import soundcloud


def accueil(request):
    """page de depart. separation entre les deux sites."""
    return render_to_response('festival/accueil.html', RequestContext(request))


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
    else:
        contact_form = ContactForm()

    return render_to_response('festival/contact.html', RequestContext(request, {'contact_form': contact_form}))

def news(request):
    retour = {
        'news': Article.objects.all().order_by('date')[:10]
    }
    return render_to_response('festival/_news.html', RequestContext(request, retour))


def liens(request):
    retour = {
        'liens': Lien.objects.all(),
    }
    return render_to_response('festival/liens.html', RequestContext(request, retour))

def music(request):

    morceaux = Music.objects.all()
    retour = {}
    client = soundcloud.Client(client_id='e2a74ab7f77aa8c5085561886d5e7b60')
    for morceau in morceaux: 
        soundcloud_widget = client.get('/oembed', url=morceau.lien, maxheight=150, maxwidth=400)
        morceau.player = soundcloud_widget.html
    
    retour['morceaux'] = morceaux
    
    return render_to_response('banda/music.html', RequestContext(request, retour))

def trombi(request):
    retour = {
        'membres': Membre.objects.filter(afficher=True)
    }
    return render_to_response('banda/trombi.html', RequestContext(request, retour))

def calendrier_sorties(request):
    return render_to_response('banda/', RequestContext(request))

def medias(request):
    medias = Media.objects.all()
    for media in medias:
        media.display()
        
    return render_to_response('festival/medias.html', RequestContext(request, {'medias': medias}))
    