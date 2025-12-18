from django.shortcuts import render
from django.views import View
from profiles.forms import UserRegisterForm, LoginForm, ProfileForm

# Create your views here.
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

        sign_up_form = UserRegisterForm(request.POST)

        if sign_up_form.is_valid():
            email = sign_up_form.cleaned_data.get('email')
            username = sign_up_form.cleaned_data.get('username')
            password = sign_up_form.cleaned_data.get('password1')

            user = User.objects.create_user(username=username, email=email, password=password)

            login(request, user)
            return redirect('/')
        else:
            return render(request, self.__template_name, {'sign_up_form': sign_up_form})