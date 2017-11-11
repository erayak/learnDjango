from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils import timezone

from .models import Gonderi,Person
from .forms import RegisterForm

class AnasayfaSayfaGorunumu(TemplateView):
    def get(self, request, **kwargs):
        gonderiler= Gonderi.objects.filter(y_tarihi__lte=timezone.now()).order_by('y_tarihi')
        return render(request,'index.html', {'gonderiler':gonderiler} )


class KayitOlSayfaGorunumu(TemplateView):

    def get(self, request, **kwargs):
        form = RegisterForm()
        UserData = Person.objects.all()
        return render(request,'register.html', { 'form':form, 'user':UserData } )
    
    def post(self, request, **kwargs):
        form = RegisterForm()
        p = Person()
        p.ad = request.POST['ad']
        p.soyad = request.POST['soyad']
        p.mail = request.POST['mail']
        p.sifre = request.POST['sifre']
        p.yayinla()
        return redirect('/register')