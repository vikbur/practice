# ~*~ coding: utf-8 ~*~

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
    # Example:
    # (r'^control_panel/', include('control_panel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
                       
        url(r'^$', 'library.views.books'),
        url(r'^library/$', 'library.views.books'),
        url(r'^library/books/$', 'library.views.books'),
        url(r'^library/books/(\d+)/$', 'library.views.book'),
        url(r'^library/authors/$', 'library.views.authors'),
        url(r'^library/authors/(\d+)/$', 'library.views.author'),
                       
)