from django import forms
from .models import Book  # already present

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# --------------------------------------
# ExampleForm (for demonstrating secure input handling)
# --------------------------------------
class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Comment'}),
        required=True
    )
