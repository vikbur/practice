from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'url_proj.views.home', name='home'),
    # url(r'^url_proj/', include('url_proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
     url(r'^$', 'url.views.listing', name='listing'),
     url(r'^log/(?P<temp>([-,.\w]*/)*)$','url.views.listing', name='listing'),
)
 