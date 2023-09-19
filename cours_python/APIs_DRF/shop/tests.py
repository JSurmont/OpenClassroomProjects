from unittest import mock
from django.urls import reverse_lazy, reverse
from rest_framework.test import APITestCase

from commons import helpers as ch
from shop.models import Category, Product
from shop.mocks import mock_openfoodfact_success, ECOSCORE_GRADE


class ShopAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Fruits', active=True)
        Category.objects.create(name='Légumes', active=False)

        cls.product = cls.category.products.create(name='Ananas', active=True)
        cls.category.products.create(name='Banane', active=False)

        cls.category_2 = Category.objects.create(name='Légumes', active=True)
        cls.product_2 = cls.category_2.products.create(name='Tomate', active=True)

    def get_article_list_data(self, articles):
        return [
            {
                'id': article.pk,
                'date_created': ch.format_datetime(article.date_created),
                'date_updated': ch.format_datetime(article.date_updated),
                'name': article.name,
                'product': article.product_id
            } for article in articles
        ]

    def get_product_list_data(self, products):
        return [
            {
                'id': product.pk,
                'date_created': ch.format_datetime(product.date_created),
                'date_updated': ch.format_datetime(product.date_updated),
                'name': product.name,
                'category': product.category_id,
            } for product in products
        ]

    def get_category_list_data(self, categories):
        return [
            {
                'id': category.id,
                'date_created': ch.format_datetime(category.date_created),
                'date_updated': ch.format_datetime(category.date_updated),
                'name': category.name,
                'description': '',
            } for category in categories
        ]

    def get_product_detail_data(self, product):
        return {
            'id': product.pk,
            'date_created': ch.format_datetime(product.date_created),
            'date_updated': ch.format_datetime(product.date_updated),
            'name': product.name,
            'category': product.category_id,
            'articles': self.get_article_list_data(self.product.articles.filter(active=True)),
            'ecoscore': ECOSCORE_GRADE,
        }


class TestCategory(ShopAPITestCase):

    url = reverse_lazy('categories-list')
    maxDiff = None

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.json()['results'], self.get_category_list_data([self.category, self.category_2]))

    def test_detail(self):
        url_detail = reverse('categories-detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, 200)
        expected = {
            'id': self.category.pk,
            'date_created': ch.format_datetime(self.category.date_created),
            'date_updated': ch.format_datetime(self.category.date_updated),
            'name': self.category.name,
            'products': self.get_product_list_data(self.category.products.filter(active=True)),
        }
        self.assertEqual(expected, response.json())

    def test_create(self):
        category_count = Category.objects.count()
        response = self.client.post(self.url, data={'name': 'Nouvelle catégorie'})
        self.assertEqual(response.status_code, 405)
        self.assertEqual(Category.objects.count(), category_count)


class TestProduct(ShopAPITestCase):

    url = reverse_lazy('products-list')

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_product_list_data([self.product, self.product_2]), response.json()['results'])

    def test_list_filter(self):
        response = self.client.get(self.url + '?category_id=%i' % self.category.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_product_list_data([self.product]), response.json()['results'])

    @mock.patch('shop.models.Product.call_external_api', mock_openfoodfact_success)
    def test_detail(self):
        url_detail = reverse('products-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_product_detail_data(self.product), response.json())

    def test_create(self):
        product_count = Product.objects.count()
        response = self.client.post(self.url, data={'name': 'Nouvelle catégorie'})
        self.assertEqual(response.status_code, 405)
        self.assertEqual(Product.objects.count(), product_count)

    def test_delete(self):
        response = self.client.delete(reverse('products-detail', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 405)
        self.product.refresh_from_db()
