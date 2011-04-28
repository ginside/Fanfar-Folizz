from django.conf.urls.defaults import *
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
	# Global : 
	(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
	
	# Festival :
    (r'^$', 'festival.views.index'),
	(r'^fanfar-folizz/$', 'festival.views.accueil'),
    (r'^fanfar-folizz/sponsors/$','festival.views.sponsors'),
    (r'^fanfar-folizz/liens/$','festival.views.liens'),
	(r'^fanfar-folizz/infosPratiques/$','festival.views.infos'),
    (r'^fanfar-folizz/groupes/$', 'festival.views.groupes'),
	(r'^fanfar-folizz/groupes/(?P<groupe_id>\d+)/$', 'festival.views.groupe_detail'),
    # Admin :
    (r'^admin/', include(admin.site.urls)),
	# Uncomment the admin/doc line below to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
)
