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
    path('findNotes/',views.findNotes),
    path('returnNotes/',views.returnNotes),
    path('takeBooks/',views.TakeBooks),
    path('saveBook/',views.SaveBook),
    path('showBooks/',views.showAllBooks),
    path('searchBooks/',views.SearchBooks),
    path('sellerInfo/',views.BookSellerInfo),
    path('BuyerInfo/',views.showBuyerInfo),
    path('SaveOrderDetails/',views.SaveOrderDetails),
    path('notice/',views.Notification),
]