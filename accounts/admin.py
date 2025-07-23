from django.contrib import admin

from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    """Customizing the user admin"""
    list_display = ['username', 'email', 'is_superuser', 'last_login', 'is_staff', 'is_active']
    list_filter = ['is_superuser', 'is_staff', 'is_active', 'date_joined']
    search_fields = ['username', 'email']
    ordering = ['username']
    show_facets = admin.ShowFacets.ALWAYS