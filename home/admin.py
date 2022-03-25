from django.contrib import admin
from . models import UserProfile,Topitem

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','location','age']
    list_filter = ['location','gender','age','location']
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Topitem)