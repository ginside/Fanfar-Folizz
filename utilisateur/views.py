# Create your views here.
from django.http import HttpResponse
from utilisateur.models import User
from django.template import Context, loader

def index(request):
    utilisateurs = User.objects.all()
    template = loader.get_template('utilisateur/index.html')
    context = Context({
                  'utilisateurs' : utilisateurs,
    })
    return HttpResponse(template.render(context))