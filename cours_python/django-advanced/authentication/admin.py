from django.contrib import admin

from authentication.models import User, Follow


admin.site.register(User)
admin.site.register(Follow)
