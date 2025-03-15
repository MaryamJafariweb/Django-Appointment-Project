from django.contrib import admin
from .models import Education


# Register your models here.
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'offer')
