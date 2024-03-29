import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from library.models import Book


@pytest.mark.django_db
def test_book_infos_view():
    client = Client()
    Book.objects.create(author="Jules Verne",
                        title="20 milles lieues sous les mers")
    path = reverse('infos', kwargs={'pk': 1})
    response = client.get(path)
    content = response.content.decode()

    expected_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <p>Jules Verne | 20 milles lieues sous les mers</p>
</body>
</html>"""

    assert content == expected_content
    assert response.status_code == 200
    assertTemplateUsed(response, "book_infos.html")
