from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     fields = ('title', 'excerpt')
#     prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Post, PostAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
