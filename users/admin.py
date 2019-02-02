from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms.users import UserForm
from .models.users import User

class CustomAdmin(UserAdmin):
    add_form = UserForm
    form = UserForm
    model = User

admin.site.register(User , CustomAdmin)