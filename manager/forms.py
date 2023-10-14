from django import forms 
from .models import *


class BooksForm(forms.ModelForm):
    class Meta:
        model = BooksModel
        fields = '__all__'