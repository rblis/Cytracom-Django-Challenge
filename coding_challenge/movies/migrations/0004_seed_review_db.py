# Generated by Django 4.2.11 on 2024-04-24 12:55

from django.db import migrations

def populate_db(apps, schema_editor):
    Movie = apps.get_model("movies", "Movie")
    Review = apps.get_model("movies", "Review")
    db_alias = schema_editor.connection.alias

    forrest_gump = Movie.objects.get(title="Forrest Gump")
    toy_story = Movie.objects.get(title="Toy Story")
    captain_phillips = Movie.objects.get(title="Captain Phillips")
    catch_me_if_you_can = Movie.objects.get(title="Catch Me If You Can")
    bridge_of_spies = Movie.objects.get(title="Bridge of Spies")

    Review.objects.using(db_alias).bulk_create([
        Review(full_name="John Doe", title="Great Movie", description="I really enjoyed this movie.", rating=4, movie_id=forrest_gump),
        Review(full_name="Jane Doe", title="Nice Movie", description="I really liked this movie.", rating=3, movie_id=toy_story),
        Review(full_name="Jonas Doe", title="Fun Movie", description="I really loved this movie.", rating=5, movie_id=captain_phillips),
        Review(full_name="Jen Doe", title="Cool Movie", description="I really adored this movie.", rating=5, movie_id=catch_me_if_you_can),
        Review(full_name="Jim Doe", title="Bad Movie", description="I really abhored this movie.", rating=1, movie_id=bridge_of_spies),

    ])

def empty_db(apps, schema_editor):
    Review = apps.get_model("movies", "Review")
    db_alias = schema_editor.connection.alias

    Review.objects.using(db_alias).filter(title__in=[
        "Great Movie",
        "Nice Movie",
        "Fun Movie",
        "Cool Movie",
        "Bad Movie",
    ]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_review"),
    ]

    operations = [
        migrations.RunPython(populate_db, empty_db),
    ]
