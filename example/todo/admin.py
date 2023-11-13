from django.contrib import admin
from .models import *


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "task", "title"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "author", "date_of_staging", "title"]

class TagsAdmin(admin.ModelAdmin):
    list_display = ["id", "tags", ]

class Image_Admin(admin.ModelAdmin):
    list_display = ["image", "post", ]

admin.site.register(Task, TaskAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Image, Image_Admin)