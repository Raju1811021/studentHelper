from django.urls import path
from chat import views
urlpatterns=[
    path('ask/',views.questAns),
    path('submitQuest/',views.submitQuestion),
]