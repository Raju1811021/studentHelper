from django.contrib import admin
from helper import models
# Register your models here.

admin.site.register(models.UserData)
admin.site.register(models.Notes)
admin.site.register(models.Books)
admin.site.register(models.order_detail)
admin.site.register(models.Notification)