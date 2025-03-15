from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Blog, Comment
from .forms import CommentCreateForm


# Create your views here.

class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'blog/blog.html', {'blogs': blogs})


class BlogDetailView(View):
    model = Blog
    form_class = CommentCreateForm

    def setup(self, request, *args, **kwargs):
        self.blog_instance = get_object_or_404(Blog, pk=kwargs['blog_id'], slug=kwargs['blog_slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        comments = self.blog_instance.post_comments.filter(is_reply=False)
        return render(request, 'blog/detail.html', {'blog': self.blog_instance,
                                                    'comments': comments,
                                                    'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.blog = self.blog_instance
            new_comment.save()
            messages.success(request, 'your comment is ok!', 'success')
            return redirect('blog:detail', self.blog_instance.id, self.blog_instance.slug)


