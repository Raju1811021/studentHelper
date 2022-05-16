from django.urls import path
from chat import views
urlpatterns=[
    path('ask/',views.questAns),
    path('submitQuest/',views.submitQuestion),
    path('suggest/',views.suggest),
    path('takeSuggestion/',views.takeSuggestion),
    path('submitAns/',views.submitAns),
]