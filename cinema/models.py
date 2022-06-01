from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    opens = models.DateTimeField()
    close = models.DateTimeField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=255)
    cinema = models.ForeignKey('cinema.Cinema', on_delete=models.CASCADE)
    actors = models.ManyToManyField('cinema.Actor')

    def __str__(self):
        return self.title


class Actor(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.IntegerField()
    birth_date = models.DateField()
    cinema = models.ForeignKey('cinema.Cinema', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
