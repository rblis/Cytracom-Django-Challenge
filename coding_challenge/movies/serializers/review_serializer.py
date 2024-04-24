from rest_framework import serializers
from movies.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "full_name",
            "title",
            "description",
            "rating",
            "date_created",
            "movie_id",
        )