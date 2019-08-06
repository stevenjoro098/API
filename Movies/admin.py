from django.contrib import admin
from Movies.models import Movies
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','year','category') #
    list_filter = ('category','year')
    search_fields = ('title','category')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Movies, MovieAdmin)