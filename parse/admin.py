from django.contrib import admin

from .models import UserCredentials

class UserCredentialsAdmin(admin.ModelAdmin):
    list_display = ('username', 'has_pass', 'has_cookie') 

    def has_pass(self, obj):
            return bool(obj.password)
    has_pass.boolean = True  
    has_pass.short_description = 'Password'

    def has_cookie(self, obj):
        return bool(obj.cookies)
    has_cookie.boolean = True  
    has_cookie.short_description = 'Cookies'  

admin.site.register(UserCredentials, UserCredentialsAdmin)
