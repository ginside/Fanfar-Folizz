# Create your views here.
from django.http import HttpResponse
from sponsor.models import Sponsor
from django.template import Context,loader
def liste(request):
    sponsors = Sponsor.objects.all()
    template = loader.get_template('index.html')
    context = Context({'sponsors' : sponsors})
    return HttpResponse(template.render(context))