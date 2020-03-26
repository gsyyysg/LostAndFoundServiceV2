from django.contrib import admin

# Register your models here.
from dynamic.models import Category, Dynamic

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','status','ctime')
    search_fields = ('id','name',)


@admin.register(Dynamic)
class DynamicAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','type', 'category', 'title', 'desc', 'images','location','meta', 'state', 'belongsTo', 'status','ctime')
    search_fields = ('id','user_id', 'type', 'category', 'title', 'desc','belongsTo', 'desc')