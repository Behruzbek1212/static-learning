from django.urls import path
from .views import Bmw

urlpatterns = [
    path("", Bmw),
]
