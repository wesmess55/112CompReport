from django.contrib import admin
from .models import Genre, Movie
# Register your models here.


class GenreTemplate(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


class MovieTemplate(admin.ModelAdmin):
    list_display = ("id", "title", "release_year", "price")
    list_display_links = ("id", "title")
    field = ("Title", "Genre", "Director", "Staring",
             "Release", "Created", "Synopsis", "price")


admin.site.register(Genre, GenreTemplate)
admin.site.register(Movie, MovieTemplate)