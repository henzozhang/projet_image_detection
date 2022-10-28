from django.urls import path
from . import views

app_name = "api_app"

urlpatterns = [
    path('', views.api, name= "api_app")
]
