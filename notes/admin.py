from django.contrib import admin
from .models import Note, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Note)
admin.site.register(Category, CategoryAdmin)