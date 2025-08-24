from django.urls import path, include
from .views import user_list_view

app_name = 'users'

urlpatterns = [
    path('', user_list_view, name='user_list'),
]
