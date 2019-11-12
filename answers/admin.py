from django.contrib import admin
from .models import Comment

#my classes
# class myComment(admin.ModelAdmin):
#     list_display = ('post','author','text','created_date')
#     list_display_links = ('author', 'post')
#     search_fields = ('post', 'author', 'created_date')
# Register your models here.
admin.site.register(Comment)