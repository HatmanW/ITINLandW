from django import forms
from .models import Task


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