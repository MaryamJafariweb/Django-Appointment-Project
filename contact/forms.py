from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'phone', 'subject', 'body')

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل*'}),
            'phone': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'تلفن همراه*'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع*'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام...*'})

        }
