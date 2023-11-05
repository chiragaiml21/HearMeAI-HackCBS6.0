from django.contrib import admin
from .models import Student, Avatar, Badge

admin.site.site_header = "Hear Me - A Voice To All"
admin.site.site_title = "Hear Me - A Voice To All"


# Register your models here.

# ============================== BADGES =================================

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('title', 'points_required')

    exclude = ('title',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'points')

    exclude = ('password', 'groups', 'user_permissions', 'is_staff',
               'is_superuser', 'last_login', 'date_joined')


@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

    exclude = ('title',)
