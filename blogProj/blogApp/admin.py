from django.contrib import admin

from .models import Blog


# to import blog to admin site
admin.site.register(Blog)