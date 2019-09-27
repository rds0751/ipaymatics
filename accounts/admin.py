from django.contrib import admin


from .models import *

class us(admin.ModelAdmin):
    list_display = ('refer', 'username')

class withdrawal12(admin.ModelAdmin):
    list_display = ('username', 'withdrawal' )


admin.site.register(Userprofile,us)
admin.site.register(User_account_profile)
admin.site.register(withdrawal,withdrawal12)
