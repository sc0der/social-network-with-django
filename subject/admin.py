from django.contrib import admin

# Register your models here.
from .models import Subject
class MySub(admin.ModelAdmin):
    list_display = ('name', 'time')
    list_display_links = ('name', 'time')
    search_fields = ('name', 'time')

admin.site.register(Subject, MySub)