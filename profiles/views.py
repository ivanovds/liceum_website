from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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