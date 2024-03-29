from django.urls import path
from .views import mark_favourtie, FavouriteProductListView


urlpatterns = [
    path('', FavouriteProductListView.as_view(), name='favourite-products'),
    path('mark/<int:id>/', mark_favourtie, name='mark-favourite'),
]
 