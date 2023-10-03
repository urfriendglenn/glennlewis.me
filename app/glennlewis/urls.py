from django.urls import path
from glennlewis import views

urlpatterns = [
    path("", views.home, name='home'),
]