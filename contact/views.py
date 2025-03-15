from django.shortcuts import render, redirect
from django.views import View
from .models import Info, Contact
from .forms import ContactForm
from django.contrib import messages


# Create your views here.

class ContactView(View):
    template_name = 'contact/contact.html'
    form_class = ContactForm

    def get(self, request):
        info = Info.objects.all()
        form = self.form_class
        return render(request, self.template_name, {'info': info,
                                                    'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Contact.objects.create(full_name=cd['full_name'],
                                   email=cd['email'],
                                   phone=cd['phone'],
                                   subject=cd['subject'],
                                   body=cd['body'])
            messages.success(request, 'Your messages send!', 'success')
            return redirect('contact:contact')
