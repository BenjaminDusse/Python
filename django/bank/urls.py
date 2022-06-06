from django.urls import path
from bank import views

urlpatterns = [
    path("", views.home, name="home"),
]
