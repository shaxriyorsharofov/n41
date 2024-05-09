from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')


class Info(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'info.html')

    def post(self):
        pass#2024-05-23T12:21:01.686Z


