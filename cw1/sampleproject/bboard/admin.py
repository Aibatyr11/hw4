from django.contrib import admin

# Register your models here.
from .models import *


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'published', 'rubric')
    list_display_links = ('title', 'price')
    search_fields = ('title', 'price')


admin.site.register(Rubric)
admin.site.register(Bb, BbAdmin)
