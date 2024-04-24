from django.db import models
from django.db.models import Avg
from datetime import time

class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    runtime = models.PositiveIntegerField()
    release_date = models.DateField()

    @property
    def runtime_formatted(self):
        return "%d:%d" % ((self.runtime // 60), (self.runtime % 60)) \
            if self.runtime > 0 else "0:00"
    
    @property
    def avg_rating(self):
        return self.review_set.aggregate(Avg("rating", default=1))["rating__avg"]
        