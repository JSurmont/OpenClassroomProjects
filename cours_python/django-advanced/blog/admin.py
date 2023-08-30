from django.contrib import admin

from blog.models import Blog, Photo, BlogContributor


admin.site.register(Blog)
admin.site.register(Photo)
admin.site.register(BlogContributor)
