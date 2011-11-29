from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'horse.events.views.homepage'),
    (r'^event/$', 'horse.events.views.event_list'),
    (r'^event/(?P<event_id>\d+)/$', 'events.views.detail'),

    (r'^riders/$', 'horse.riders.views.rider_list'),
    (r'^riders/(?P<rider_id>\d+)/$', 'horse.riders.views.detail'),

    (r'^schools/$', 'horse.schools.views.school_list'),
    (r'^schools/(?P<school_id>\d+)/$', 'horse.schools.views.detail'),

    # url(r'^horse/', include('horse.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
