from django.http import HttpResponse
from datetime import date 
from django.shortcuts import render_to_response
# page de depart. separation entre les deux sites.
def index(request):
    urlFestival,urlBanda = "/FanfarFolizz","/BandaTchitchaa"
    retour = {'date' : date.today(),'urlFestival' : urlFestival,'urlBanda' : urlBanda}
    return render_to_response('festival/index.html',retour)

