from django.test import TestCase

from Netflix.film.models import Actor, Movie
from Netflix.film.serializers import ActorSerializer, MovieSerializer


class TestActorModels(TestCase):
    def setUp(self) -> None:
        pass

    def test_actor_name(self):
        a = Actor.objects.get(id=1)
        malumot = Actor(a)
        assert malumot.data['name'] == 'Will Smith'

    def test_actor_gender(self):
        a = Actor.objects.get(id=1)
        malumot = Actor(a)
        assert malumot.data['gender'] == 'erkak'

    def test_actor_birth_date(self):
        a = Actor.objects.get(id=1)
        malumot = Actor(a)
        assert malumot.date['birth_date'] == '25.09.1968'


class TestActorSerializer(TestCase):
    def setUp(self) -> None:
        pass

    def test_artist(self):
        a = Actor.objects.all()
        malumot = ActorSerializer(a, many=True)
        assert malumot.data['id'] == 1


class TestMovieSerializer(TestCase):
    def setUp(self) -> None:
        pass

    def test_movie(self):
        m = Movie.objects.all()
        malumot = MovieSerializer(m, many=True)
        assert malumot.data['id'] == 1