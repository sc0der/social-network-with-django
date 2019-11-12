from django.contrib import admin
from .models import Person, Friend

#my classes
class myFr(admin.ModelAdmin):
    list_display = ("current_user",)
    search_fields = ('current_user',)

class MyUser(admin.ModelAdmin):
    list_display = ('username','f_name','avatar', 'unis','gen','person','city', 'birth_date', 'admin')
    readonly_fields = ['image_img']
    list_display_links = ('username','unis')
    search_fields = ('user', 'email', 'birth_date')
# Register your models here.
admin.site.register(Person, MyUser)
admin.site.register(Friend, myFr)