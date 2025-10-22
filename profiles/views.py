from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from profiles.forms import UserRegisterForm


class RegisterView(View):
    def __init__(self):
        super().__init__()
        self.__template_name = ...#add a template

    def get(self, request, *args, **kwargs):
        form = ... # form needed here!
        return render(request, self.__template_name, {'form': form})

    @classmethod
    def validate_user(cls, username, password):
        if User.objects.filter(username=username, password=password).exists():
            raise ValueError('Hehe, you can`t create several same users')

    @classmethod
    def save_user(cls, form, username, password):
        extra_fields = form.cleaned_data.pop('password1').pop('password2').pop('username')
        User.objects.create_user(username, password=password, **extra_fields)

    def post(self, request, *args, **kwargs):
        if request.POST is None:
            raise ValueError('No POST data got!')

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            self.validate_user(username, password)
            self.save_user(form, username, password)

        return HttpResponseRedirect('redirect url')


def login_view(request):
    print(request)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Вітаємо, {user.username}!")
            return redirect(request.GET.get('next', 'home'))
        else:
            messages.error(request, "Невірне ім’я користувача або пароль.")
            return render(request, "login.html")

    return render(request, "login.html")


@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')
