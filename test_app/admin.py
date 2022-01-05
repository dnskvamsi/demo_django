from django.contrib import admin
from test_app.models import Customer, Employee

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "balance"]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "dept", "salary"]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)
