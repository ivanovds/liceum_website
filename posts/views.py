from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .forms import PostForm
from .models import Post


class NewPostView(View):
    def __init__(self):
        super().__init__()
        self.__template_name = 'new_post.html'

    def get(self, request, *args, **kwargs):
        post_form = PostForm()
        return render(request, self.__template_name, {'post_form': post_form})

    def post(self, request, *args, **kwargs):
        if request.POST is None:
            raise ValueError('No POST data got!')

        post_form = PostForm(request.POST, request.FILES or None)

        if post_form.is_valid():
            author = self.request.user
            image = post_form.cleaned_data.get('image')
            main_text = post_form.cleaned_data.get('main_text')

            Post.objects.create(author=author, image=image, main_text=main_text)

            return HttpResponseRedirect('/posts/')
        else:
            return render(request, self.__template_name)


class PostsView(ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        return context