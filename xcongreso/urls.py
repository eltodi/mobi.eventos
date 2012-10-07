from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'maint.views.home', name='maint_home'),
    #url(r'^plantilla/', include('plantilla.foo.urls')),
    #url(r'^404/$', 'maint.views.error404', name='error404'),
    url(r'^agenda/$', 'maint.views.agenda', name='maint_agenda'),

    url(r'^ponentes/(\d+)/$', 'maint.views.ponente', name='maint_ponente'),
    url(r'^ponentes/$', 'maint.views.ponentes', name='maint_ponentes'),
    
    url(r'^stands/$', 'maint.views.feria', name='maint_feria'),
    url(r'^stands/(\d+)/$', 'maint.views.stand', name='maint_stand'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
