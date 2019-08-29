# -*- coding: utf-8 -*-

from django.shortcuts import render


def home(request):
    return render(request, 'base1.html')

def about(request):
    return render(request, 'core/about.html')

def digi(request):
    return render(request, 'core/digi.html')

def seo(request):
    return render(request, 'core/seo.html')

def smo(request):
    return render(request, 'core/smo.html')

def tour(request):
    return render(request, 'core/index.html')

def ppc(request):
    return render(request, 'core/ppc.html')

def web(request):
    return render(request, 'core/web.html')

def dev(request):
    return render(request, 'core/dev.html')

def out(request):
    return render(request, 'core/out.html')

def brand(request):
    return render(request, 'core/brand.html')

def content(request):
    return render(request, 'core/content.html')

def logo(request):
    return render(request, 'core/logo.html')

def video(request):
    return render(request, 'core/video.html')

def webp(request):
    return render(request, 'core/webp.html')

def digip(request):
    return render(request, 'core/digip.html')

def add(request):
    return render(request, 'core/add.html')

def client(request):
    return render(request, 'core/client.html')

def why(request):
    return render(request, 'core/why.html')

def career(request):
    return render(request, 'core/career.html')

def contact(request):
    return render(request, 'core/contact.html')
