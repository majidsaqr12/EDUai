from django.shortcuts import render
from .models import Offer

def home(request):
    offers = Offer.objects.all()
    return render(request, 'pages/home.html', {'offers': offers})

def custom_404(request):
    return render(request, 'pages/404.html', status=404)

def success_view(request):
    return render(request, 'pages/success.html')
