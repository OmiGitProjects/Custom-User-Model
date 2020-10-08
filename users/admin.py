from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomAdminForm(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User Roles',
            {
                'fields' : (
                    'is_director',
                    'is_producer',
                )
            }
        )
    )

admin.site.register(CustomUser, CustomAdminForm)