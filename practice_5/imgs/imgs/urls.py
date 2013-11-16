from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^library/$', 'booksimage.views.books'),
    url(r'^library/books/$', 'booksimage.views.books'),
    url(r'^library/books/(\d+)/$', 'booksimage.views.book'),
    url(r'^library/authors/$', 'booksimage.views.authors'),
    url(r'^library/authors/(\d+)/$', 'booksimage.views.author'),
    # Examples:
    # url(r'^$', 'imgs.views.home', name='home'),
    # url(r'^imgs/', include('imgs.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
