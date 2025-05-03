from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.ImageField(upload_to="actor_img")
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Genre(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Movie(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movie/')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    year = models.IntegerField(default=2019)
    country = models.CharField(max_length=50)
    budget = models.IntegerField()

    def __str__(self):
        return self.name



