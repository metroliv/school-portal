from django.contrib import admin
from .models import School, Class, Stream, Student

# Inline classes for related models
class ClassInline(admin.TabularInline):
    model = Class
    extra = 1

class StreamInline(admin.TabularInline):
    model = Stream
    extra = 1

class StudentInline(admin.TabularInline):
    model = Student
    extra = 1

# Registering models with custom admin classes
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    inlines = [ClassInline]

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    list_filter = ('school',)
    search_fields = ('name', 'school__name')
    inlines = [StreamInline]

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'school_class')
    list_filter = ('school_class',)
    search_fields = ('name', 'school_class__name')
    inlines = [StudentInline]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'stream')
    list_filter = ('stream',)
    search_fields = ('first_name', 'last_name', 'stream__name')

#Registering other custom admin classes if needed
#admin.site.register(School)
#admin.site.register(Class)
#admin.site.register(Stream)
#admin.site.register(Student)

