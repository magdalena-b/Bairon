from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from backend.models import Poem
from backend.models import POETS

import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs) -> None:

        f = open('whitman.txt','r')
        poems = f.read()

        poem = Poem.objects.get_or_create(text=poems, author=POETS[3][0])

        f = open('shakespeare_sonnets.txt','r')
        poems = f.read()

        poem = Poem.objects.get_or_create(text=poems, author=POETS[1][0])

        f = open('cummings.txt','r')
        poems = f.read()

        poem = Poem.objects.get_or_create(text=poems, author=POETS[2][0])


