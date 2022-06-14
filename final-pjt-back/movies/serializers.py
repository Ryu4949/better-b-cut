from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies import models as movie_models
from django.db.models import Max
import collections

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = movie_models.Movie
        fields  = ('id', 'title', 'overview', 'release_date', 'vote_average', 'poster_path', 'genre',)
        read_only_fields  = ('id', 'vote_average',)
        #fields = '__all__'


class UserRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = movie_models.UserRating
        fields  = ('rating',)

