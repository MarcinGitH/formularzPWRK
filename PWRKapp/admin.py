from django.contrib import admin
from .models import Employee, Entry
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):

    list_filter = ("username", "admin_accesss",)
    list_display = ("username", "admin_accesss",)
   # prepopulated_fields = {"slug": ("title",)}


admin.site.register(Employee, EmployeeAdmin)
