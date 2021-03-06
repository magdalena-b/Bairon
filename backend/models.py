from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

POETS = [
    ("Machine", "Machine"),
    ("Shakespeare", "Shakespeare"),
    ("Cummings", "Cummings"),
    ("Whitman", "Whitman"),
    ("Lorem Ipsum", "Lorem Ipsum")
]


# class Poet(models.Model):
#     name = models.CharField(choices=POETS, default=POETS[0], max_length=100)

class Input(models.Model):
    style = models.CharField(choices=POETS, default=POETS[0], max_length=100)
    # style = models.ForeignKey(Poet, on_delete=models.DO_NOTHING, null=True, blank=True)
    first_line = models.CharField(max_length=1000, null=True, blank=True)
    model_type = models.CharField(max_length=100, default="gpt2")
    # TODO another input options
    keywords = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self) -> str: return self.style + " | " + self.first_line

    def __str__(self):
        if self.style != None and self.first_line != None:
            return self.style + " | " + self.first_line
        else:
            return ""


class Poem(models.Model):
    author = models.CharField(choices=POETS, default=POETS[0], max_length=100)
    # author = models.ForeignKey(Poet, on_delete=models.DO_NOTHING, null=True, blank=True)
    input = models.ForeignKey(Input, on_delete=models.DO_NOTHING, null=True, blank=True)
    text = models.CharField(max_length=100000, default="")
    views = models.IntegerField(default=0)
    sentiment = models.CharField(max_length=100, null=True, blank=True)
    generator_type = models.CharField(max_length=100, default="full")
    style_transfer = models.IntegerField(default=0)
    translations = models.CharField(max_length=100000, default="", blank=True)
    bleu_score = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('views',)
    
    def __str__(self) -> str:
        return str(self.id) + " | " + str(self.author)


class Rate(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    rate = models.IntegerField()
    category = models.CharField(default="overall", max_length=100)



class TuringTestVote(models.Model):
    VOTES = [
        ("Human", "Human"),
        ("Machine", "Machine")
    ]

    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    fragment = models.CharField(max_length=200, null=True, blank=True)
    vote = models.CharField(choices=VOTES, default="Machine", max_length=100)

