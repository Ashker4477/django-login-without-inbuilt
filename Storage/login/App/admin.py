from django.contrib import admin
from .models import reg


class AppAdmin(admin.ModelAdmin):
    list_display = ("fn", "ln", "em", "Dob", "img")


# Register your models here.
admin.site.register(reg, AppAdmin)
