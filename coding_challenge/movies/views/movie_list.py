from rest_framework.generics import ListCreateAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        filter = self.request.GET.get("filter", None)
        runtime = self.request.GET.get("runtime", None)

        if runtime and filter == "greater-than":
            return Movie.objects.filter(runtime__gt=runtime)
        elif runtime and filter == "less-than":
            return Movie.objects.filter(runtime__lt=runtime)
        else:
            return Movie.objects.order_by("id")