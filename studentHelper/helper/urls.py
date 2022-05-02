from django.urls import path
from helper import views
urlpatterns=[
    path('home/',views.homePage),
]