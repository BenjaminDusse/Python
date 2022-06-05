from django.urls import path, include
from bank import views


urlpatterns = [
    path("", views.home, name="home"),
]
