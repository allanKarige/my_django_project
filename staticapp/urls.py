from django.urls import path
from . import views
import time

urlpatterns = [
    path('', views.static_app)
]

