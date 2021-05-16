from django.shortcuts import render, HttpResponseRedirect
from django.views import View


class FaqView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'faq.html')
        else:
            return HttpResponseRedirect('/login')
