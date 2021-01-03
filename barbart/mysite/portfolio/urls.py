from django.urls import path
from . import views
from .views import HomeView, NapkinView, NapkinDetailView, GobelinView, GobelinDetailView, TableclothView, TableclothDetailView, CoverlateView, CoverlateDetailView, AboutView, ChristmasView, ChristmasDetailView, EasterView, EasterDetailView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('serwety', NapkinView.as_view(), name='napkin'),
    path('serwety/<int:pk>', NapkinDetailView.as_view(), name='napkin-detail'),
    path('gobeliny', GobelinView.as_view(), name='gobelin'),
    path('gobeliny/<int:pk>', GobelinDetailView.as_view(), name='gobelin-detail'),
    path('obrusy', TableclothView.as_view(), name='tablecloth'),
    path('obrusy/<int:pk>', TableclothDetailView.as_view(), name='tablecloth-detail'),
    path('narzuty', CoverlateView.as_view(), name="coverlate"),
    path('narzuty/<int:pk>', CoverlateDetailView.as_view(), name='coverlate-detail'),
    path('bozeNarodzenie', ChristmasView.as_view(), name='christmas'),
    path('bozeNarodzenie/<int:pk>', ChristmasDetailView.as_view(), name='christmas-detail'),
    path('wielkanoc', EasterView.as_view(), name='easter'),
    path('wielkanoc/<int:pk>', EasterDetailView.as_view(), name='easter-detail'),
    path('kontakt', views.ContactView, name='contact'),
]