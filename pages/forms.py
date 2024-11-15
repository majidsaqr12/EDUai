from django import forms
from .models import ContactMessage, Appointment

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'complaint_type', 'message']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'id': 'full-name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'id': 'email'}),
            'complaint_type': forms.Select(choices=[
                ('Complaint 1', 'Complaint 1'),
                ('Complaint 2', 'Complaint 2'),
                ('Complaint 3', 'Complaint 3'),
            ], attrs={'id': 'complaint-type'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'id': 'message', 'rows': 4}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'email', 'phone', 'appointment_date', 'appointment_time']

        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }