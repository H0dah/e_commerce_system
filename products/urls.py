from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [
    path('', views.ProductList.as_view, name='product_get_or_post'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
