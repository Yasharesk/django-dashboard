from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # TODO: Check how the 'next' variable was set
            # if request.GET.get('next'):
            #     return HttpResponseRedirect(reverse(request.GET.get('next')))
            return HttpResponseRedirect(reverse('home:home'))
        else:
            context = {
                'username': username,
                'error': 'No user with this credentials'
            }
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home:home'))
        context = {}
        return render(request, 'accounts/login.html', context)
# TODO: Create Login view


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
