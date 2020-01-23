from django import forms
from .models import Note


class NotesModelForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['user', 'timestamp']
