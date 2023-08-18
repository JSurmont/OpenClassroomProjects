from django.http import HttpResponse
from django.shortcuts import render
from .models import Band
from .models import Listing


def hello(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/hello.html',
                  {'bands': bands})


def about(request):
    return render(request,
                  'listings/about-us.html')


def listings(request):
    all_listings = Listing.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'all_listings': all_listings})


def contact(request):
    return render(request,
                  'listings/contact.html')
