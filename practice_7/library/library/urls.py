from django.conf.urls import patterns, include, url
from orders.views import CustomersList, CustomerDetails
from books.views import BookList, AuthorList, BookDetail, AuthorDetail
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="utils/map.html")),
    url(r'^library/$', BookList.as_view()),
    url(r'^library/books/$', BookList.as_view()),
    url(r'^library/books/(?P<pk>\d+)/$', BookDetail.as_view()),
    url(r'^library/authors/$', AuthorList.as_view()),
    url(r'^library/authors/(?P<pk>\d+)/$', AuthorDetail.as_view()),
    url(r'^orders/$', CustomersList.as_view()),
    url(r'^orders/(?P<pk>\d+)/$', CustomerDetails.as_view(template_name="orders/customer.html")),
    url(r'^registration/$', 'registration.views.registrate'),
    url(r'^login/$', 'registration.views.log_in'),
    # Examples:
    # url(r'^$', 'imgs.views.home', name='home'),
    # url(r'^imgs/', include('imgs.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
