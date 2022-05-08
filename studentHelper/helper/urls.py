from django.urls import path
from helper import views
urlpatterns=[
    path('home/',views.homePage),
    path('UserPass/',views.UsernamePass),
    path('userregistered/',views.UserRegister),
    path('userLogin/',views.UserLogin),
    path('userLogout/',views.UserLogout),
    path('shareNotes/',views.shareNotes),
    path('submitNotes/',views.submitNotes),
]