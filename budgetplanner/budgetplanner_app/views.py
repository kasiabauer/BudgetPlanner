from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        ctx = {
            'id': 1,
            'name': 'name'
        }
        return render(request, 'home.html', ctx)
