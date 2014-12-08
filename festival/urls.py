from django.conf.urls import patterns, include
from festival import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from captcha import urls

admin.autodiscover()

urlpatterns = patterns('',

                       # Global :
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

                       # Festival :
                       (r'^$', 'festival.views.index'),
                       (r'^fanfar-folizz/$', 'festival.views.accueil'),
                       (r'^fanfar-folizz/sponsors/$', 'festival.views.sponsors'),
                       (r'^fanfar-folizz/liens/$', 'festival.views.liens'),
                       (r'^fanfar-folizz/infosPratiques/$', 'festival.views.infos'),
                       (r'^fanfar-folizz/groupes/$', 'festival.views.groupes'),
                       (r'^fanfar-folizz/groupes/(?P<groupe_id>\d+)/$', 'festival.views.groupe_detail'),
                       (r'^fanfar-folizz/activite/(?P<activite_id>\d+)/$', 'festival.views.activite_detail'),
                       (r'^fanfar-folizz/programme/$', 'festival.views.programme'),
                       (r'^fanfar-folizz/medias/$', 'festival.views.medias'),
                       (r'^fanfar-folizz/historique/$', 'festival.views.historique'),
                       (r'^fanfar-folizz/news/$', 'festival.views.news'),
                       (r'^fanfar-folizz/contact/$', 'festival.views.contact'),
                       # Admin :
                       (r'^admin/', include(admin.site.urls)),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^captcha/', include('captcha.urls'))
)

