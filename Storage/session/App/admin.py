from django.contrib import admin
from .models import User


class AppAdmin(admin.ModelAdmin):
    list_display = ("Name", "DateOfBirth", "Email")



admin.site.register(User, AppAdmin)
