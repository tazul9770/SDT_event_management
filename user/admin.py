from django.contrib import admin
from user.models import CustomUser

admin.site.register(CustomUser)

# @admin.register(CustomUser)
# class AdminUser(admin.ModelAdmin):
#     list_display=('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
#     search_fields=('id', 'username', 'first_name', 'last_name')
#     list_filter=('id', 'is_staff', 'username')
