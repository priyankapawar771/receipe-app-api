from django.contrib import admin
from .models import User,Receipe
# Register your models here.
@admin.register(User)
class StudentsAdmin(admin.ModelAdmin):
        list_display = ['name','email']

@admin.register(Receipe)
class ReceipeAdmin(admin.ModelAdmin):
        list_display = ['user','title','description','time_minutes','price']
