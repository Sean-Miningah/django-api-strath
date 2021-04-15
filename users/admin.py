from django.contrib import admin
from .models import User


@admin.register(User)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('email', 'id', 'user_name', 'phone_number',)
    list_filter = (
        'gender', 'date_created', 'active', 'followers', 'following',
    )

    readonly_fields = ('date_created',)
    search_fields = ('id', 'email', 'user_name', 'phone_number',)
    fieldsets = (
        (None, {
            'fields': (
                'id', 'email', 'user_name', 'active',
            ),
        }),
        ('More Details', {
            'classes': ('collapse',),
            'fields': (
                'phone_number', 'date_created', 'profile_image',
                'gender', 'bio',
            ),
        }),
        ('User Statistics', {
            'classes': ('collapse',),
            'fields': (
                'followers', 'following',
            ),
        }),
    )
    readonly_fields = (
        'id', 'followers', 'following', 'date_created', 'profile_image',
        'email', 'user_name'
    )
