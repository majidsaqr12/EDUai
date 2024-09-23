from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html', status=404)

def custom_404(request):
    return render(request, 'pages/404.html', status=404)

def success_view(request):
    return render(request, 'pages/success.html')
