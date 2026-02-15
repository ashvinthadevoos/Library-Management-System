from django import forms
from books import models

class BookCreateForm(forms.ModelForm):
    date=forms.DateField(
        input_formats=['%d-%m-%Y']
    )
    class Meta:
        model=models.Books
        exclude=['is_active']