from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact

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

        # check if same query has been made for the same listing by the same user
        if request.user.is_authenticated:
            if Contact.objects.all().filter(user_id=user_id, listing_id=listing_id).exists():
                messages.error(request, 'You have submitted inquery for the same listing before')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # send email
        send_mail(
            'Property listing inquery',
            'There has been an inquery for ' + listing + '. Sign into the admin panel for more info.',
            'haohong@gmail.com',
            [realtor_email, 'receiver@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/listings/'+listing_id)
