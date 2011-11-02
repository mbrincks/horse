from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'horseproject.eventsapp.views.homepage'),
    (r'^event/$', 'horse.events.views.event_list'),

    # url(r'^horse/', include('horse.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
