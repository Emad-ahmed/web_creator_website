from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from myapp.forms import LoginForm
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            fm = LoginForm()
            return render(request, 'login.html', {'form': fm})
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

        return render(request, 'login.html', {'form': fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')
