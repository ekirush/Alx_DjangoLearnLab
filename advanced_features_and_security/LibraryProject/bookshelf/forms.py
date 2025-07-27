from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '200'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if any(tag in title.lower() for tag in ['<script>', '</script>', 'javascript:']):
            raise forms.ValidationError("Invalid input detected in title.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if any(tag in author.lower() for tag in ['<script>', '</script>', 'javascript:']):
            raise forms.ValidationError("Invalid input detected in author field.")
        return author

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year and (year < 0 or year > 3000):
            raise forms.ValidationError("Please enter a valid publication year.")
        return year
