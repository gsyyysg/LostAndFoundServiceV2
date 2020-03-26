from django.contrib import admin

# Register your models here.
from user.models import User, UserOpenid

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','stu_id','nick_name','avatar','gender','phone','status','role','ctime')
    search_fields = ('id','stu_id','nick_name','phone')

@admin.register(UserOpenid)
class UserOpenidAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','openid','status','ctime')
    search_fields = ('id','user_id','openid')