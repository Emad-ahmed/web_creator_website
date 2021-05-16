from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class SettingsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'setting.html')
        else:
            return HttpResponseRedirect('/login')
