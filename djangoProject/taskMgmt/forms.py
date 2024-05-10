#forms.py
from django import forms
from .models import Task
from .models import Profile


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'due_time', 'urgent', 'important', 'description']
        widgets = {
            'due_date': forms.DateInput(format='%m/%d/%Y', attrs={'type': 'date'}),
            'due_time': forms.TimeInput(attrs={'type': 'time'}),
            'urgent': forms.RadioSelect(choices=[(True, 'Urgent'), (False, 'Not Urgent')]),
            'important': forms.RadioSelect(choices=[(True, 'Important'), (False, 'Not Important')]),
        }
        help_texts = {
            'first_name': 'Enter your first name (e.g., John).',
            'last_name': 'Enter your last name (e.g., Doe).',
            'phone_number': 'Enter your phone number (e.g., +1234567890).',
            'bio': 'Write a brief description about yourself.',
            'location': 'Enter your current city or region.',
            'birth_date': 'Provide your birth date (YYYY-MM-DD).',
        }

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'John'}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Doe'}),
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '+1234567890'}),
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Write a brief description about yourself.'}),
    )
    location = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'City, Country'}),
    )
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
    )
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number', 'bio', 'location', 'birth_date']