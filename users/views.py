from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import \
    UserCreationForm


def register(request):
    """registration new user """
    if request.method != 'POST':
        # show empty form
        form = UserCreationForm()
    else:
        # show not empty form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()

            # login, to homepage
            login(request, new_user)
            return redirect('')


def user_signin(request):
    if request.method == 'POST':
        return render(request, 'users/user_signin.html')
        # form = LoginForm(data=)
    return render(request, 'users/user_signin.html')

# изменить по типу registration
def user_signup(request):
    if request.method == 'POST':
        return render(request, 'users/user_signup.html')
        # form = LoginForm(data=)
    return render(request, 'users/user_signup.html')
