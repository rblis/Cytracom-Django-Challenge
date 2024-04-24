from rest_framework import serializers
from movies.models import Movie, Review
from .review_serializer import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):
    runtime_formatted = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    reviews = ReviewSerializer(source="review_set", many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "release_date",
            "runtime_formatted",
            "avg_rating",
            "reviews",
        )
    
    def get_runtime_formatted(self, obj):
        return obj.runtime_formatted
    
    def get_avg_rating(self, obj):
        return obj.avg_rating