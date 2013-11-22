# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from orders.models import Order, Customer


class CustomersList(ListView):
    #greeting = "Good Day"

    #def get(self, request):
        #return HttpResponse(self.greeting)
    model = Order
    context_object_name = 'orders'


class CustomerDetails(DetailView):
    #model = Order
    context_object_name = 'order'
    queryset = Order.objects.all()
