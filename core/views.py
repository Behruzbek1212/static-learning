from django.shortcuts import render
from .models import Car

def Bmw(request):
    malumotlar = Car.objects.all()
    qolib = {
        "malumot": malumotlar
    }


    return render(request, "bmw.html", qolib)

