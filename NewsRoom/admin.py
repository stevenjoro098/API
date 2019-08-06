from django.contrib import admin
from django.contrib import *

from NewsRoom.models import NewsRoom

# Register your models here.
class NewsRoomAdmin(admin.ModelAdmin):
    list_display = ('title','location')
    list_filter = ('location',)
    search_fields = ('title',)
    prepopulated_fields = {'slug':('title',)}

admin.site.register(NewsRoom,NewsRoomAdmin)
'''
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ["newsroom"]
    def newsroom(self,obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
            )
        )'''