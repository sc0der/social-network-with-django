from django.shortcuts import render, redirect, get_object_or_404
from	django.http	import	HttpResponse
from .models import Person, Friend
from django.conf import settings
from questions.models import Savolho
from	django.contrib.auth.decorators	import	login_required
from .forms import UserRegisterForm, UserEditForm, UserLoginForm
from django.contrib.auth import logout, login, authenticate
# login_vew
def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                 password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("dashboard")
                else:
                    return HttpResponse('Неактивный пользователь')
            else:
                return HttpResponse('Неправилный ввод логина или пароля')
    else:
        form = UserLoginForm()
    return render (request, 'registration/login.html', {'form':form})
# registration_view
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request = request,
                    template_name = "accounts/register.html",
                    context={"form":form})

# dashboard_view
@login_required
def	dashboard(request):
    savoli = Savolho.objects.all()
    inform = Person.objects.all()
    return	render(request, 'accounts/dashboard.html', {'inform': inform, 'savoli':savoli})
@login_required
def edit(request):
    if request.method == 'POST':
        edit_form = UserEditForm(instance=request.user, data=request.POST)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('dashboard')
    else:
        edit_form = UserEditForm(instance=request.user)
    return render(request, 'accounts/edit.html', {'edit_form':edit_form})

@login_required
def	user_list(request):
    user_p	=	Person.objects.filter(is_active=True)
    return	render(request, 'accounts/friends.html', {'section':	'people', 'user_p':	user_p})

@login_required
def	user_detail(request,	username):
    prof	=	get_object_or_404(Person, username=username, is_active=True)
    post = Savolho.objects.filter(author=prof.id)
    return	render(request, 'accounts/profile.html', {'section':	'people', 'prof':	prof, 'post':post})


def recapcha(request):
    return render(request, 'index.html', {'site_key': settings.RECAPTCHA_SITE_KEY})