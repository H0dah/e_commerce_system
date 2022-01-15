from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import UserCreate


urlpatterns = [
    path('signup', UserCreate.as_view(), name='register'),
    path('login', obtain_auth_token)
]
