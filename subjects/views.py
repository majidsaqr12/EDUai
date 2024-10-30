from django.shortcuts import render

def subjects_view(request):
    return render(request, 'subjects/subjects.html')

