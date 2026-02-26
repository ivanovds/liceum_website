from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from profiles.forms import UserRegisterForm, LoginForm, ProfileForm

from .forms import PostForm
from .models import Post


@method_decorator(login_required, name='dispatch')
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


class UpdatePostView(View):
    def __init__(self):
        super().__init__()
        self.__template_name = 'update_post.html'

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        post_form = PostForm(instance=post)
        return render(request, self.__template_name, {'post_form': post_form})

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.POST is None:
            raise ValueError('No POST data got!')

        post_form = PostForm(request.POST, request.FILES or None, instance=post)
        if post_form.is_valid():
            post_form.save()

            return redirect('/')
        else:
            return render(request, self.__template_name, {'post_form': post_form})


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class PostsDetailedView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user == self.object.author
        return context