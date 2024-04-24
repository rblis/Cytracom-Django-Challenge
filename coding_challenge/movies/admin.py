from django.contrib import admin

from movies.models import Movie, Review

@admin.register(Movie)
class MovieAdminConsole(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "runtime",
        "release_date",
    )

@admin.register(Review)
class ReviewAdminConsole(admin.ModelAdmin):
    list_display = (
        "full_name",
        "title",
        "description",
        "rating",
        "date_created",
        "movie_id",
    )