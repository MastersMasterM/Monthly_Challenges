from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "main"),
    path("<int:month>", views.month_num),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]