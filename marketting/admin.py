from django.contrib import admin
from .models import SignUp


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ("email",)

