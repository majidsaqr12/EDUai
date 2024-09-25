from django.shortcuts import render, redirect
from .models import Offer, Testimonial, FAQCategory
from .forms import ContactForm

def home(request):
    offers = Offer.objects.all()
    testimonials = Testimonial.objects.all()
    testimonials_per_slide = 3
    total_slides = (len(testimonials) + testimonials_per_slide - 1) // testimonials_per_slide
    
    categories = FAQCategory.objects.prefetch_related('faq_set').all() 

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  

    return render(request, 'pages/home.html', {
        'offers': offers,
        'testimonials': testimonials,
        'total_slides': total_slides,
        'categories': categories, 
        'form': form 
    })


def custom_404(request):
    return render(request, 'pages/404.html', status=404)

def success_view(request):
    return render(request, 'pages/success.html')
