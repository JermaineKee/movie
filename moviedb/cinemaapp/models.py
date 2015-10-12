from django.db import models

# Create your models here.

class Rater(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    (
        (MALE, 'M'),
        (FEMALE, 'F'),

    )
    age = models.PositiveSmallIntegerField()
    occupation = models.CharField(max_length=40)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return (self.id)


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('rating'))['rating__avg']

    def __str__(self):
        return '{}'.format(self.title)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()

    def __str__(self):
        return 'Rater {}, Title: {}, Rating: {}'.format
        (self.rater, self.movie, self.rating)


def load_user_data():
    import csv
    import json
    import re

    users = []

    with open('ml-1m/users.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split(
                                    '::'),
                                delimiter='\t')

        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'cinemaapp.Rater',
                'pk': int(row['UserID']),
            }

            users.append(user)

        with open('user.json', 'w') as f:
            f.write(json.dumps(users))


def load_movie_data():
    import csv
    import json
    movies = []

    with open('ml-1m/movies.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split(
                                    '::'),
                                delimiter='\t')
        for row in reader:
            movie = {
                'fields': {
                    'title': row['Title'],
                },
                'model': 'cinemaapp.Movie',
                'pk': int(row['MovieID']),
            }
            movies.append(movie)

        with open('movies.json', 'w') as f:
            f.write(json.dumps(movies))


def load_ratings_data():
    import csv
    import json
    ratings = []

    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating::Timestamp'
                                .split('::'),
                                delimiter='\t')
        for row in reader:
            rating = {
                'fields': {
                    'rater': row['UserID'],
                    'movie': row['MovieID'],
                    'rating': row['Rating'],
                },
                'model': 'cinemaapp.Rating',
            }
            ratings.append(rating)

    with open('ratings.json', 'w') as f:
        f.write(json.dumps(ratings))
