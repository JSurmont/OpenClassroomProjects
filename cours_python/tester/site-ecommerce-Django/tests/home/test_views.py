from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
import pytest


@pytest.fixture
def client():
    client = Client()
    return client


def test_redirect_home_view(client):
    """
    Testing if our RedirectHomeView redirects successfully (status_code 302)
    For the second assert, We are testing if we redirect to the '/home/' url
     """
    response = client.get(reverse('redirect_home'))

    assert response.status_code == 302
    assert response.url == '/home/'


@pytest.mark.django_db
def test_HomeView(client):
    """
    In the first assert, We are testing if our get request returns 200 (OK) status code
    For the second assert, we are making sure that our view returns the home.html template
    """
    response = client.get(reverse('home'))

    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')
