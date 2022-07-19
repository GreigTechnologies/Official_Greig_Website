from django.shortcuts import render
from .models import client, hero, heroabout
from .models import about
from .models import herosec
from .models import fleetmap
from .models import iridummap
from .models import shipdetail
from .models import client


# Create your views here.

def oil(request):
    herodata = hero.objects.all()[0]
    heroaboutdata = heroabout.objects.all()[0]
    aboutdata = about.objects.all()
    clientdata = client.objects.all()

    context = {
        'hero' : herodata,
        'heroabout' : heroaboutdata,
        'about' : aboutdata,
        'client' : clientdata,
    }
    return render(request, 'service/oil.html', context)

def iridium(request):
    herodata = hero.objects.all()[1]
    herosecdata = herosec.objects.all()
    iridummapdata = iridummap.objects.all()[0]
    
    context = {
        'hero' : herodata,
        'herosec' : herosecdata,
        'iridummap' : iridummapdata,
    }
    return render(request, 'service/iridium-mobile.html', context)

def fleet(request):
    herodata = hero.objects.all()[2]
    heroaboutdata = heroabout.objects.all()[1]
    fleetmapdata = fleetmap.objects.all()[0]
    
    
    context = {
        'hero' : herodata,
        'heroabout' : heroaboutdata,
        'fleetmap' : fleetmapdata
    }

    return render(request, 'service/fleet_broadband.html', context)

def ship(request):
    herodata = hero.objects.all()[3]
    shipdetaildata = shipdetail.objects.all()

    context = {
        'hero' : herodata,
        'shipdetail' : shipdetaildata
    }

    return render(request, 'service/ship_security.html', context)

def video(request):
    return render(request, 'service/oil.html')

def voice(request):
    return render(request, 'service/oil.html')