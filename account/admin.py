from account.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django import forms

class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
        self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75)

class AccountAdmin(UserAdmin):
    add_form = UserCreationFormExtended
    add_fieldsets = (
        (
            None, {
                'classes': ('wide', ),
                'fields': ('email', 'username', 'password1', 'password2',)
            }
        ),
    )
    list_display = ('email', 'username', 'is_active', 'date_joined')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username', )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, AccountAdmin)