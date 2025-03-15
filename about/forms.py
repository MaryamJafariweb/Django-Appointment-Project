from django import forms
from .models import Comments


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'image', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی*'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل*'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام...*'})

        }