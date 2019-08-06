from django.contrib import admin
from Music.models import Music
# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title','artist','genre','album')

    search_fields = ('title','genre')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Music, MusicAdmin)