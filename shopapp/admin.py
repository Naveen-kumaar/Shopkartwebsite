from django.contrib import admin
from .models import Category
from .models import Product

# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name','image','description')

# admin.site.register(Category,CategoryAdmin)

admin.site.register(Category)
admin.site.register(Product)
