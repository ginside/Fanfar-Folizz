from django.conf.urls import patterns, include
from festival import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from captcha import urls

admin.autodiscover()

urlpatterns = patterns('',
                       # Global :
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

                       # Banda :
                       (r'^$', 'banda.views.accueil'),
                       (r'^liens/$', 'banda.views.liens'),
                       (r'^trombi/$', 'banda.views.trombi'),
                       (r'^music/$', 'banda.views.music'),
                       (r'^medias/$', 'banda.views.medias'),
                       (r'^news/$', 'banda.views.news'),
                       (r'^contact/$', 'banda.views.contact'),
                       (r'^calendrier/$', 'banda.views.calendrier_sorties'),
                       # Admin :
                       (r'^admin/', include(admin.site.urls)),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^captcha/', include('captcha.urls')),
)

