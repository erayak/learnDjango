from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Gonderi

class AnasayfaSayfaGorunumu(TemplateView):
    def get(self, request, **kwargs):
        gonderiler= Gonderi.objects.filter(y_tarihi__lte=timezone.now()).order_by('y_tarihi')
        return render(request,'index.html', {'gonderiler':gonderiler} )