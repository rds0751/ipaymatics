# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^digi$', views.digi, name='digi'),
    url(r'^seo$', views.seo, name='seo'),
    url(r'^smo$', views.smo, name='smo'),
    url(r'^ppc$', views.ppc, name='ppc'),
    url(r'^web$', views.web, name='web'),
    url(r'^dev$', views.dev, name='dev'),
    url(r'^out$', views.out, name='out'),
    url(r'^brand$', views.brand, name='brand'),
    url(r'^content$', views.content, name='content'),
    url(r'^logo$', views.logo, name='logo'),
    url(r'^video$', views.video, name='video'),
    url(r'^webp$', views.webp, name='webp'),
    url(r'^digip$', views.digip, name='digip'),
    url(r'^add$', views.add, name='add'),
    url(r'^client$', views.client, name='client'),
    url(r'^why$', views.why, name='why'),
    url(r'^career$', views.career, name='career'),
    url(r'^about$', views.about, name='about'),
    url(r'^tour', views.tour, name='tour')
]
