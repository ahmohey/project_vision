from django.contrib import admin

# Register your models here.
from .models.user import User


class UserAdmin(admin.ModelAdmin):
  list_display = ("user_id", "user_name","user_email")
  
admin.site.register(User, UserAdmin)