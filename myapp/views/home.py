from django.shortcuts import render, HttpResponseRedirect
from django.views import View


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            return HttpResponseRedirect('/login')
