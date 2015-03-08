# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from banda.models import Lien, Article, Media
from banda.forms import ContactForm


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
    return render_to_response('banda/liens.html', RequestContext(request, retour))


def music(request):
    return render_to_response('', RequestContext(request))

def trombi(request):
    return render_to_response('banda/trombi.html', RequestContext(request))

def calendrier_sorties(request):
    return render_to_response('banda/', RequestContext(request))

def medias(request):
    medias = Media.objects.all()
    for media in medias:
        media.display()
        
    return render_to_response('festival/medias.html', RequestContext(request, {'medias': medias}))
    