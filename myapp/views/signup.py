from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from myapp.forms import SignForm


class SignupView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            fm = SignForm()
            return render(request, 'signup.html', {'form': fm})
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        fm = SignForm(request.POST)
        if fm.is_valid():
            fm.save()
        return render(request, 'signup.html', {'form': fm})
