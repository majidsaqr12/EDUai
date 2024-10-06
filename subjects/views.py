from django.shortcuts import render
from .models import Mathematics, English, Chemistry, Geography, Science, History, Biology, Physics, Arabic, French

def subjects_view(request):
    subjects = {
        'mathematics': Mathematics.objects.first(),
        'english': English.objects.first(),
        'chemistry': Chemistry.objects.first(),
        'geography': Geography.objects.first(),
        'science': Science.objects.first(),
        'history': History.objects.first(),
        'biology': Biology.objects.first(),
        'physics': Physics.objects.first(),
        'arabic': Arabic.objects.first(),
        'french': French.objects.first(),
    }
    return render(request, 'subjects/subjects.html', subjects)
