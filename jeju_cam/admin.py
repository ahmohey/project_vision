from django.contrib import admin

# Register your models here.
from jeju_cam.models.user import User


class UserAdmin(admin.ModelAdmin):
  list_display = (
    "user_id",
    "user_name",
    "user_email"
  )
  
admin.site.register(User, UserAdmin)

'''
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ("student_no", "name")


'''