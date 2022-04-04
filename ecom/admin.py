from django.contrib import admin
from .models import Customer, Product, Orders, Feedback, Warehouse, Worker, WorkPerformed, Currency, Calculation, \
    UnitsOfMeasurement, Material


# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Orders, OrderAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.


# ================================================== >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ================================================== >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class WarehouseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Warehouse, WarehouseAdmin)


class WorkerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Worker, WorkerAdmin)


class WorkPerformedAdmin(admin.ModelAdmin):
    pass


admin.site.register(WorkPerformed, WorkPerformedAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Currency, CurrencyAdmin)


class CalculationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Calculation, CalculationAdmin)


class UOMAdmin(admin.ModelAdmin):
    pass


admin.site.register(UnitsOfMeasurement, UOMAdmin)


class Materialdmin(admin.ModelAdmin):
    pass


admin.site.register(Material, Materialdmin)