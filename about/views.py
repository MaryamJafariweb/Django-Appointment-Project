from django.shortcuts import render, redirect
from django.views import View
from .models import About, Comments
from .forms import CommentCreateForm
from django.contrib import messages


# Create your views here.
class AboutView(View):
    def get(self, request):
        info = About.objects.all()
        form = CommentCreateForm()
        comments = Comments.objects.all()
        return render(request, 'about/about.html', {'info': info,
                                                    'form': form, 'comments': comments})

    def post(self, request):
        form = CommentCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Comments(name=form.cleaned_data['name'],
                     body=form.cleaned_data['body'],
                     image=request.FILES['image']).save()
            messages.success(request, 'نظر شما به ثبت رسید!', 'success')
            return redirect('home:home')

