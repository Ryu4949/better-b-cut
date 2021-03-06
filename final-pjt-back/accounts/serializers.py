from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Article, Comment

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email',)
