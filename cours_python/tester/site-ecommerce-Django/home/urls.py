from django.urls import path

from .views import HomeView, redirect_home_view


urlpatterns = [
    path('', redirect_home_view, name='redirect_home'),
    path('home/', HomeView.as_view(), name='home'),
]
