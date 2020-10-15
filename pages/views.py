from django.shortcuts import render

# Create your views here.

def index(request):


    context = {}
    template_name = 'pages/index.html'
    return render(request,template_name, context)


def about(request):


    context = {}
    template_name = 'pages/about.html'
    return render(request,template_name, context)



