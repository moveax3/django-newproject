from django.contrib import admin
from .models import Target

@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'parent', 'target_type')
