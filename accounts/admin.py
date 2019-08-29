from django.contrib import admin


from .models import *

class us(admin.ModelAdmin):
    list_display = ('refer', 'username')

admin.site.register(Userprofile,us)
