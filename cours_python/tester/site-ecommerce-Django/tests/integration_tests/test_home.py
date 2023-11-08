from django.urls import reverse, resolve
from django.test import Client

from home.views import redirect_home_view, HomeView
from products.models import Product

from pytest_django.asserts import assertTemplateUsed
import pytest


CLIENT = Client()


@pytest.mark.django_db
def test_slash_route():
    """
    Our test approach starts with testing the 'redirect_home' route, whether it maps to 'redirect_home_view'
    or not, then we test if redirect_home_view redirected to '/home/' route.
    Next we test if 'home' route maps to 'HomeView' and we check if the HomeView renders the 'home.html' template,
    also we check if it is rendering the data from the correct model (Product)
    """
    # Testing if the 'redirect_home' route maps to 'redirect_home_view'
    url = reverse('redirect_home')
    assert resolve(url).func, redirect_home_view

    # Testing if 'redirect_home_view' redirected to '/home/' route
    response = CLIENT.get(reverse('redirect_home'))
    assert response.status_code == 302
    assert response.url == '/home/'

    # Testing if 'home' route maps to 'HomeView'
    url = reverse('home')
    assert resolve(url).func.view_class, HomeView

    # Testing if 'HomeView' renders the correct template 'home.html' and with the correct model (Product)
    response = CLIENT.get(reverse('home'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
    assert HomeView.model == Product


@pytest.mark.django_db
def test_home_route():
    """
    For this test approach, we are simply testing if 'home' route maps to 'HomeView',
    and the 'HomeView' renders the correct template 'home.html' and with the correct model (Product)
    """
    # Testing if 'home' route maps to 'HomeView'
    url = reverse('home')
    assert resolve(url).func.view_class, HomeView

    # Testing if 'HomeView' renders the correct template 'home.html' and with the correct model (Product)
    response = CLIENT.get(reverse('home'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
    assert HomeView.model == Product
    