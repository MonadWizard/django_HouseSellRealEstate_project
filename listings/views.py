from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Paginator

from listings.choices import price_choices, bedroom_choices, state_choices


from .models import Listing
# Create your views here.

def index(request):
    # listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)  # earlyer first & see all published only

    paginator = Paginator(listings, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    paged_listing = paginator.get_page(page_number)

    context = {'listings':paged_listing}
    template_name = 'listings/listings.html'
    return render(request,template_name, context)



def listing(request, listing_id):
    # if page not available then show 404
    listing = get_object_or_404(Listing, pk=listing_id)  # (model,pk)


    context = {'listing':listing}
    template_name = 'listings/listing.html'
    return render(request,template_name, context)



def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)   # search enter description

    # citys
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)   # search enter description

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)   # search enter description

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)   # search enter description

    # bedrooms
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)   # search enter description



    context = {
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list, 
        'values': request.GET ,

    }
    template_name = 'listings/search.html'
    return render(request,template_name, context)


