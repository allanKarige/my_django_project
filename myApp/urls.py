from django.urls import path
from . import views

urlpatterns = [
    path("", views.guidance),
    path("hello", views.Hello, name="Hello"),
    path("emobilis", views.emobilis),
    path("home", views.home),
]