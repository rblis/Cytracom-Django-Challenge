from django.urls import path

from movies.views import MovieListView, MovieDetailView

urlpatterns = [
    path("", MovieListView.as_view(), name="MovieListView"),
    path("<int:id>",  MovieDetailView.as_view(), name="MovieDetailView")
]