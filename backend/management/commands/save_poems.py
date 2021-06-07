from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from backend.models import Poem
from backend.models import POETS

class Command(BaseCommand):
    def handle(self, *args, **kwargs) -> None:

        f = open('ginsberg.txt','r')
        poems = f.read()

        poem = Poem(text=poems, author=POETS[2])
        poem.save()
        
