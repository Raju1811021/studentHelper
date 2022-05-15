import email
from operator import mod
from django.db import models
from django.contrib.auth.models import User

#contains all user related information
class UserData(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=25)
    collage_name=models.CharField(max_length=50)
    type=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return self.name

#contain all Notes in pdf form
class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    notes_pdf=models.FileField(null=False)
    subject=models.CharField(max_length=100)
    def __str__(self):
        return self.subject

# Containing Books
class Books(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    book_name=models.CharField(max_length=100,null=False)
    book_img=models.ImageField()
    author=models.CharField(max_length=100,null=False)
    price=models.CharField(max_length=6,null=False)
    edition=models.DateField()
    def __str__(self):
        return self.book_name

#Book Order Details
class order_detail(models.Model):
    order_no=models.AutoField(primary_key=True)
    Book_id=models.CharField(max_length=100,unique=True)
    Buyer_id=models.CharField(max_length=100)
    seller_id=models.CharField(max_length=100)
    date=models.DateField()
    quantity=models.CharField(max_length=10)
    delivery_address=models.CharField(max_length=1000)
    payment_status=models.CharField(max_length=10)
    def __str__(self):
        return self.Book_id


