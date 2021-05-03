from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Poet(models.Model):
    NAMES = [
        ("Plain", "Plain"),
        ("Shakespeare","Shakespeare"),
        ("Cummings","Cummings"),
        ("Dickinson","Dickinson"),
    ]

    name = models.CharField(choices=NAMES, default=NAMES[0], max_length=100, primary_key=True)


class Input(models.Model):
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE)
    first_line = models.CharField(max_length=100)
    # TODO another input options
    keywords = models.CharField(max_length=100, null=True, blank=True)


class Poem(models.Model):
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, default="")
    views = models.IntegerField(default=0)


class Rate(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.DO_NOTHING)
    rate = models.IntegerField(validators=[models.MinValueValidator(1), models.MaxValueValidator(10)])


class TuringTestVote(models.Model):
    VOTES = [
        ("Human", "Human"),
        ("Machine", "Machine")
    ]

    poem = models.ForeignKey(Poem, on_delete=models.DO_NOTHING)
    fragment = models.CharField(max_length=200, null=True, blank=True)
    vote = models.CharField(choices=VOTES, default="Machine", max_length=100)

