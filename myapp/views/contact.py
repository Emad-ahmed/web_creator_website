from django.shortcuts import render, HttpResponseRedirect
from django.views import View


class ContactView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'contact.html')
        else:
            return HttpResponseRedirect('/login')
