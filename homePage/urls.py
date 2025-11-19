from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeView.as_view(), name='home'),
]