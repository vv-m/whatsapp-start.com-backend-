from django.contrib import admin
from users.models import User, Template


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'is_active')
    search_fields = ('email',)
    # list_filter = ('category',)
    # empty_value_display = '-пусто-'


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'name')
    # search_fields = ('text',)
    # list_filter = ('category',)
    # empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Template, TemplateAdmin)
