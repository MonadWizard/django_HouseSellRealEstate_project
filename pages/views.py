from django.shortcuts import render
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]  # take last 3 listings


    context = {
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        }
    template_name = 'pages/index.html'
    return render(request,template_name, context)


def about(request):

    realtors = Realtor.objects.order_by('-hire_date')  # get all realtors
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)  # get MVP realtors


    context = {'realtors':realtors, 'mvp_realtors':mvp_realtors}
    template_name = 'pages/about.html'
    return render(request,template_name, context)



