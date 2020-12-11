from django.urls import path
from . import views

urlpatterns = [
    # views.pyのindex関数を返す
    path("", views.index, name="home")
]