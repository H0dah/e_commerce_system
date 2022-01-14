from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'api/users$', views.UserCreate.as_view(), name='user-create'),
]