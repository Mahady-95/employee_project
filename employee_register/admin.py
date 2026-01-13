from django.contrib import admin

# Register your models here.
from .models import Employee, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("fullname", "emp_code", "mobile", "position")
    search_fields = ("fullname", "emp_code")
    list_filter = ("position",)
