from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Room)
admin.site.register(models.Client)
admin.site.register(models.BookedRoom)
