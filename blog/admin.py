from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import *
import csv

# from django.contrib.auth import get_user_model

class UserAdmin(UserAdmin):
    model = MyUser
    actions=['download_csv']
    list_display = ('username', 'email', 'first_name', 'last_name',)
    list_filter = ('is_superuser','is_active')
    fieldsets = (
        (None, {"fields": ('username', 'email', 'first_name', 'last_name',)}),)


    def download_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    download_csv.short_description = "Export CSV"


class TagAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    list_filter = ('name','slug')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    list_filter = ('name','slug')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'comment',
                    'created_date', 'parent',)
    list_filter = ('name', 'email', 'post', 'comment',
                   'created_date', 'parent',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'author', 'title', 'created_date','slug',
                    'published_date', 'feature_image', 'thumbnail_image',)
    list_filter = ('category', 'author', 'created_date', 'published_date',)


admin.site.register(MyUser, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Post, PostAdmin)
