from django.contrib import admin
from .models import Complex, Repair, Category, Side, Portfolio, Call

@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    list_display = ['complex', 'price', 'description']

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ['repair', 'price', 'unit', 'recat', 'reside', 'main']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(Side)
class SideAdmin(admin.ModelAdmin):
    list_display = ['side']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['picture', 'text']

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ['client', 'phone', 'date']

