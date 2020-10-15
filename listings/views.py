from django.shortcuts import render

# Create your views here.

def index(request):


    context = {}
    template_name = 'listings/listings.html'
    return render(request,template_name, context)



def listing(request):


    context = {}
    template_name = 'listings/listing.html'
    return render(request,template_name, context)



def search(request):


    context = {}
    template_name = 'listings/search.html'
    return render(request,template_name, context)


