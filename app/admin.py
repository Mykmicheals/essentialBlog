from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Post)
# admin.site.register(AdminPost)
admin.site.register(Comment)
admin.site.register(SliderPost)
admin.site.register(Categories)
admin.site.register(Description)
admin.site.register(Profile)
admin.site.register(News)
