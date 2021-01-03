from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Home, Napkin, Gobelin, Tablecloth, Coverlate, About, Christmas, Easter
class HomeView(ListView):
    model = Home
    template_name = 'home.html'

class NapkinView(ListView):
    model = Napkin
    template_name = 'napkin.html'

class NapkinDetailView(DetailView):
    model = Napkin
    template_name = 'napkinDetail.html'

class GobelinView(ListView):
    model = Gobelin
    template_name = 'gobelin.html'

class GobelinDetailView(DetailView):
    model = Gobelin
    template_name = 'gobelinDetail.html'

class TableclothView(ListView):
    model = Tablecloth
    template_name = 'tablecloth.html'

class TableclothDetailView(DetailView):
    model = Tablecloth
    template_name = 'tableclothDetail.html'

class CoverlateView(ListView):
    model = Coverlate
    template_name = 'coverlate.html'

class CoverlateDetailView(DetailView):
    model = Coverlate
    template_name = 'coverlateDetail.html'

class AboutView(ListView):
    model = About
    template_name = 'about.html'

class ChristmasView(ListView):
    model = Christmas
    template_name = 'christmas.html'

class ChristmasDetailView(DetailView):
    model = Christmas
    template_name = 'christmasDetail.html'

class EasterView(ListView):
    model = Easter
    template_name = 'easter.html'

class EasterDetailView(DetailView):
    model = Easter
    template_name = 'easterDetail.html'


def ContactView(request):
    return render(request, 'contact.html')