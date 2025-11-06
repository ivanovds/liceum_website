from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User

from profiles.forms import UserRegisterForm, LoginForm, ProfileForm
from profiles.models import Profile


class RegisterView(View):
    def __init__(self):
        super().__init__()
        self.__template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        sign_up_form = UserRegisterForm()
        return render(request, self.__template_name, {'sign_up_form': sign_up_form})

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


def login_view(request):
    login_form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
        else:
            messages.error(request, "User not found")

    return render(request, "login.html", {'login_form': login_form})


@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')


def home_view(request):
    return render(request, "home.html")


class ProfileView(View):
    def __init__(self):
        super().__init__()
        self.__template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        profile_form = ProfileForm()
        return render(request, self.__template_name, {'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        if request.POST is None:
            raise ValueError('No POST data got!')

        profile_form = ProfileForm(request.POST)

        if profile_form.is_valid():
            role = profile_form.cleaned_data.get('role')
            class_number = profile_form.cleaned_data.get('class_number')
            class_name = profile_form.cleaned_data.get('class_name')
            date_of_birth = profile_form.cleaned_data.get('date_of_birth')
            bio = profile_form.cleaned_data.get('bio')
            interesting_facts = profile_form.cleaned_data.get('interesting_facts')

            user = request.user
            Profile.objects.update_or_create(user=user, defaults={'role': role, 'class_number': class_number, 'class_name': class_name, 'date_of_birth': date_of_birth, 'bio': bio, 'interesting_facts': interesting_facts})
            return redirect('/')
        else:
            return render(request, self.__template_name, {'sign_up_form': profile_form})