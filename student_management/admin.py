# admin.py

from django.contrib import admin
from .models import Student, Mark

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'phone', 'location', 'hobby')
    search_fields = ('name', 'email', 'location',)

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks_obtained')
    list_filter = ('student', 'subject')
    search_fields = ('student__name', 'subject')
    raw_id_fields = ('student',)
