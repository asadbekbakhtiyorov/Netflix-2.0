from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Actor, Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'date', 'actor']


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'gender', 'birth_date']
    def validate_gender(self, se):
        if se != 'erkak' or se != 'ayol':
            raise ValidationError(detail='Se most be erkak or ayol')
        return se


