from django.contrib import admin

from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'is_superuser',
        'is_staff',
        'is_active'
    ]


admin.site.register(CustomUser, UserAdmin)