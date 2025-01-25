from django.contrib import admin

from .models import Category, Item

#class itemdata(admin.ModelAdmin):
 #   list_display=("name","id")

admin.site.register(Category)
admin.site.register(Item)

