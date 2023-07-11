from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
# 관리자 페이지에 Post 모델 반영
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
