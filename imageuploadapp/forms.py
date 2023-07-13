from django import forms

from .models import img

class image(forms.ModelForm):
    class Meta:
        model=img
        fields = '__all__'
        labels = {'photo':''}