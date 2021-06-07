from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status, views
from rest_framework.decorators import api_view
from django.core.serializers import serialize, json
from django.forms.models import model_to_dict

import random

from .serializers import *

import sys
sys.path.insert(0, '..')
try:
    from NLP.model import poem_generator
except Exception as e:
    raise(e)


# Create your views here.

@api_view(['GET', 'POST', ])
def test(request: Request) -> Response:
    return Response({"status": "ok"}, status=status.HTTP_200_OK)


class GeneratePoemView(generics.CreateAPIView):
    serializer_class = InputSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request, *args, **kwargs):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            input = serializer.create(serializer.validated_data)

            try:
                text, sentiment = poem_generator.generate(
                        style = input.style,
                        first_line=input.first_line
                )
                
                poem = Poem(
                    input = input,
                    text = text,
                    sentiment = sentiment
                )

                return Response(model_to_dict(poem), status=status.HTTP_200_OK)

            except Exception as e:
                print(e)
                return Response(status=status.HTTP_403_FORBIDDEN)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SavePoem(generics.CreateAPIView):
    serializer_class = PoemSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request, *args, **kwargs):
        data = request.data
        data["author"] = "Machine"
        data["sentiment"] = data.get("sentiment", "normal")
        serializer = PoemSerializer(data=data)
        if serializer.is_valid():
            created = serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PoemView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request, id):
        try:
            poem = Poem.objects.get(id=id)
            poem.views += 1
            poem.save()
            data = model_to_dict(poem)
            try:
                data["first_line"] = poem.input.first_line
                data["style"] = poem.input.style
            except:
                pass
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RatingView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request, id = None):
        try:
            if id:
                poem = Poem.objects.get(id=id)
                result = {}
                result["rate-average"] = poem.rate_set.all().aggregate(models.Avg('rate'))["rate__avg"]
                result["rate-count"] = len(poem.rate_set.all())
                result["TT-human"] = len(poem.turingtestvote_set.filter(vote="Human"))
                result["TT-machine"] = len(poem.turingtestvote_set.filter(vote="Machine"))
                return Response(result, status=status.HTTP_200_OK)
            else:
                result = {}
                result["rate-average"] = Rate.objects.all().aggregate(models.Avg('rate'))["rate__avg"]
                result["rate-count"] = len(Rate.objects.all())
                result["TT-human"] = len(TuringTestVote.objects.filter(vote="Human"))
                result["TT-machine"] = len(TuringTestVote.objects.filter(vote="Machine"))
                return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PoemListView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request, style = None, sentiment = None, number = 10):
        try:
            poems = Poem.objects.all()
            if style:
                poems = poems.filter(input__style=style)
            if sentiment:
                poems = poems.filter(sentiment=sentiment)
            result = {"all": []}
            for poem in list(poems.order_by('-views'))[:number]:
                result["all"].append({"id": poem.id, "input": poem.input.first_line, "text": poem.text, "style": poem.input.style})
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateRate(generics.CreateAPIView):
    serializer_class = RateSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request, *args, **kwargs):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            created = serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateTuringTestVote(generics.CreateAPIView):
    serializer_class = TuringTestVoteSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request, *args, **kwargs):
        serializer = TuringTestVoteSerializer(data=request.data)
        if serializer.is_valid():
            created = serializer.create(serializer.validated_data)
            print(created)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TuringTestFragmentView(views.APIView):
    
    permission_classes = (AllowAny,)

    def get(self, request: Request, id = None):
        try:
            coin_toss = random.randint(0, 1)
            result = {}

            if coin_toss == 0:
                poems = Poem.objects.filter(author="Machine")
                correct = "Machine"

            else:
                poems = Poem.objects.filter(author="Shakespeare") | Poem.objects.filter(author="Ginsberg") | Poem.objects.filter(author="Cummings")
                correct = "Human"

            coin_toss = random.randint(0, 1)
            result = {}

            poem = random.choice(poems)
            
            result['id'] = poem.id
            lines = poem.text.split('\n')
            lines_formatted = [line for line in lines if not line.isspace()]

            text = random.choice(lines_formatted).strip()
            result['text'] = text

            result["correct"] = correct
            
            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


