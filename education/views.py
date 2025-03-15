from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Education
from .forms import CommentForm
from django.contrib import messages
from ordering.forms import CartAddForm


# Create your views here.

class EducationListView(View):
    def get(self, request):
        educations = Education.objects.filter(is_active=True)
        return render(request, 'education/education.html', {'educations': educations})


class DetailEducationView(View):
    form_class = CommentForm
    template_name = 'education/detail.html'

    def setup(self, request, *args, **kwargs):
        self.education_instance = get_object_or_404(Education, pk=kwargs['education_id'], slug=kwargs['education_slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        comments = self.education_instance.comment.all()
        form_cart = CartAddForm()
        return render(request, self.template_name, {'details': self.education_instance,
                                                    'comments': comments,
                                                    'form': self.form_class,
                                                    'form_cart': form_cart})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.education = self.education_instance
            new_comment.save()
            messages.success(request, 'your comment is ok!', 'success')
            return redirect('education:education_detail', self.education_instance.id, self.education_instance.slug)
        # return render(request, self.template_name, {'details': self.education_instance,
        #                                             'form': self.form_class})
