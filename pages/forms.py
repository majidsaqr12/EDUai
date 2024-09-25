from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'complaint_type', 'message']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'complaint_type': forms.Select(choices=[
                ('Complaint 1', 'Complaint 1'),
                ('Complaint 2', 'Complaint 2'),
                ('Complaint 3', 'Complaint 3'),
            ], attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control', 'rows': 4}),
        }
