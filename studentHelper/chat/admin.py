from django.contrib import admin
from chat import models
# Register your models here.
admin.site.register(models.answer)
admin.site.register(models.question)