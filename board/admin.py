from django.contrib import admin

from .models import *

@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'username', 'is_staff', 'is_active']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
