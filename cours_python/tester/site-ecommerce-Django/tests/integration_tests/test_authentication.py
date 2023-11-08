import pytest

from django.urls import reverse
from django.test import Client
from django.contrib import auth


@pytest.mark.django_db
def test_login_route():
    client = Client()

    # Inscrire un utilisateur à l’aide de la vue `signup` afin de l’enregistrer dans la base de données
    credentials = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'TestUser',
        'email': 'testuser@testing.com',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    client.post(reverse('signup'), credentials)

    # Connecter cet utilisateur avec la vue `login`
    response = client.post(reverse('login'), {'username': 'TestUser', 'password': 'TestPassword'})

    # Vérifier que la redirection vers la page d’accueil est effectuée
    assert response.status_code == 302
    assert response.url == reverse('home')

    # Vérifier que l’utilisateur est bien authentifié
    user = auth.get_user(client)
    assert user.is_authenticated
