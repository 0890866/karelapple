from django.contrib import admin
from .models import AppleType
from .models import Recipe

# Register your models here.

admin.site.register(AppleType)
admin.site.register(Recipe)
