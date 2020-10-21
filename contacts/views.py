from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail

from .models import Contacts
# Create your views here.

def contact(request):
    
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(
                listing_id=listing_id, user_id=user_id)

            if has_contacted:
                messages.error(request, 'You have already inquiry')
                return redirect('/listings/'+listing_id)



        contact = Contacts(listing=listing, listing_id=listing_id, name=name,
                email=email, phone=phone, message=message, user_id=user_id )

        contact.save()

        # Send email   # set sending mail name & password to settings.py on last portions
        send_mail(
            'Subject here',
            'Here is' +listing+ 'the message.',
            'rcareleess@gmail.com',
            [realtor_email, 'rcareleess@gmail.com'],
            fail_silently=False,
        )


        messages.success(request, 'Your request has been submitted..!')
        return redirect('/listings/'+listing_id)








