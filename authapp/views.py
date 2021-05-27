from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from authapp.models import User

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket


#def login(request):
#    if request.method == 'POST':
#        form = UserLoginForm(data=request.POST)
#        if form.is_valid():
#            username = request.POST['username']
#            password = request.POST['password']
#            user = auth.authenticate(username=username, password=password)
#            if user and user.is_active:
#                auth.login(request, user)
#                return HttpResponseRedirect(reverse('index'))
#    else:
#        form = UserLoginForm()
#    context = {'title': 'GeekShop - Авторизация', 'form': form}
#    return render(request, 'authapp/login.html', context)
class UserLoginView(LoginView):
    model = User
    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')

#def register(request):
#    if request.method == 'POST':
#        form = UserRegisterForm(data=request.POST)
#        if form.is_valid():
#            form.save()
#            messages.success(request, 'Вы успешно зарегистрировались')
#            return HttpResponseRedirect(reverse('users:login'))
#    else:
#        form = UserRegisterForm()
#    context = {'title': 'GeekShop - Регистрация', 'form': form}
#    return render(request, 'authapp/register.html', context)

class UserRegisterView(CreateView):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения успешно сохранены')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'GeekShop - Личный кабинет',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, "authapp/profile.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
