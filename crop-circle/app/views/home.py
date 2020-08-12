
from django.views.generic import View
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy

class HomeView(View):
    def get(self, request):
        return HttpResponseRedirect(reverse_lazy('search'))