from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل*'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام...*'})

        }