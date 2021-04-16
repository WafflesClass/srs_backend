from django.contrib import admin
from myapp.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(DemoModel)
admin.site.register(User, UserAdmin)
