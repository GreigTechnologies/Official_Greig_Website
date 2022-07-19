from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import about
from.models import slider
from .models import whyus
from .models import whyusinfo
from .models import service
from .models import team
from .models import partner
from .models import bg
from .models import footerinfo
from .models import contactform

# Create your views here.

def Home(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contactformdata = contactform(name=name,email=email,subject=subject,message=message)
        contactformdata.save()


    aboutdata = about.objects.all()
    sliderdata = slider.objects.all()
    whyusdata = whyus.objects.all()[0]
    whyusinfodata = whyusinfo.objects.all()
    servicedata = service.objects.all()
    teamdata = team.objects.all()
    partnerdata = partner.objects.all()
    bgdata = bg.objects.all()
    footerinfodata = footerinfo.objects.all()[0]
    context = {
        'about': aboutdata,
        'slider': sliderdata,
        'whyus' : whyusdata,
        'whyusinfo' : whyusinfodata,
        'service' : servicedata,
        'team' : teamdata,
        'partner' : partnerdata,
        'bg' : bgdata,
        'footerinfo' : footerinfodata,
    }

    return render(request, 'index.html', context)

def aboutus(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contact.html')