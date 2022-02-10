from django.db import models

# Create your models here.


class Actor(models.Model):
    G = (
        ('erkak', 'erkak'),
        ('ayol', 'ayol')
    )
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=G)

    def __str__(self):
        return self.name


class Movie(models.Model):
    gen = (
        ('action', 'action'),
        ('drama', 'drama'),
        ('comedy', 'comedy'),
    )
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=12, choices=gen)
    date = models.DateField()
    actor = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title