from django.contrib import admin
from .models import Savolho

#my classes
class myQuestions(admin.ModelAdmin):
    list_display = ('title','published','subject','author')
    list_display_links = ('author','title')
    search_fields = ('author', 'title', 'subject')
# Register your models here.
admin.site.register(Savolho, myQuestions)
# Register your models here.
