from django.contrib import admin
from .models import Category, Article, Post, MyModel, Staff, UserProfile

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'category__name')
    list_filter = ('category',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'phone', 'location', 'hobby', 'gender')
    search_fields = ('name', 'email', 'location',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image')
    search_fields = ('user__username',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
