from django.db import models


class Author(models.Model):

    class Sex(models.IntegerChoices):

        MALE: int = 0, 'Male'
        FEMALE: int = 1, 'Female'
        OTHER: int = 2, 'Other'

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    sex = models.PositiveIntegerField(choices=Sex.choices)
    date_of_birth = models.DateField()


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='books')
    name = models.CharField(max_length=150)
    description = models.TextField()
    release_date = models.DateField()
