from django.contrib import admin
from .models import Register


class AppAdmin(admin.ModelAdmin):
    list_display = ("Fullname", "Profile")


admin.site.register(Register, AppAdmin)


