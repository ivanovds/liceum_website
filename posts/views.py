from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
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

        post_form = PostForm(request.POST)

        if post_form.is_valid():
            author = self.request.user
            image = post_form.cleaned_data.get('image')
            main_text = post_form.cleaned_data.get('main_text')

            Post.objects.create(author=author, image=image, main_text=main_text)

            return HttpResponseRedirect('/')  # TODO: add redirect url to posts list
        else:
            return render(request, self.__template_name)
