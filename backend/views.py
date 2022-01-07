from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status, views
from rest_framework.decorators import api_view
from django.core.serializers import serialize, json
from django.forms.models import model_to_dict
from rest_framework import serializers
from rest_framework.throttling import AnonRateThrottle

import random

from .serializers import *
from NLP.statistics_helper import statisticsHelper

import sys
sys.path.insert(0, '..')
try:
    from NLP.model import poem_generator
except Exception as e:
    raise(e)


# Create your views here.

@api_view(['GET', 'POST', 'PUT'])
def test(request: Request) -> Response:
    return Response({"status": "ok"}, status=status.HTTP_200_OK)


class GeneratePoemView(generics.CreateAPIView):
    # throttle_scope = 'generate'

    serializer_class = InputSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request, *args, **kwargs):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            input = serializer.create(serializer.validated_data)
            print(input)

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

class GeneratePoemLineView(generics.CreateAPIView):
    serializer_class = InputSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request, *args, **kwargs):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            input = serializer.create(serializer.validated_data)
            print(input)

            try:
                text, sentiment = poem_generator.generate_line(
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

    def put(self, request: Request):
        try:
            poem_generator.clear_collab_lines_cache()
            return Response(status=status.HTTP_200_OK)
        except:
           return Response(status=status.HTTP_400_BAD_REQUEST) 





class GenerateStyleTransferView(generics.CreateAPIView):
    serializer_class = InputSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request, *args, **kwargs):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            input = serializer.create(serializer.validated_data)
            print(input)
            try:
                from simpletransformers.t5 import T5Model
                args = {
                    "overwrite_output_dir": True,
                    "max_seq_length": 256,
                    "max_length": 50,
                    "top_k": 50,
                    "top_p": 0.95,
                    "num_return_sequences": 5
                }

                trained_model_path = "checkpoint/shakespeare_T5/shakespeare_T5"
                trained_model = T5Model("t5",trained_model_path,args=args, use_cuda=False)
                prefix = "paraphrase"

                # line = "When forty winters shall besiege thy brow"
                line = input.first_line
                pred = trained_model.predict([f"{prefix}: {line}"])
                result_lines = pred[0]
                # result_line = result_lines[0]

                result = {}
                result['translated_lines'] = result_lines

                return Response(result, status=status.HTTP_200_OK)

            except Exception as e:
                print(e)
                result = {}
                result['translated_lines'] = [
                    'When forty winters shall besiege thy brow',
                    'Look in thy glass and tell the face thou viewest',
                    'Unthrifty loveliness, why dost thou spend'
                ]

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
                result["TT-TH"] = len(TuringTestVote.objects.filter(vote="Human").exclude(poem__author="Machine"))
                result["TT-FH"] = len(TuringTestVote.objects.filter(vote="Human").filter(poem__author="Machine"))
                result["TT-TM"] = len(TuringTestVote.objects.filter(vote="Machine").exclude(poem__author="Machine"))
                result["TT-FM"] = len(TuringTestVote.objects.filter(vote="Machine").filter(poem__author="Machine"))
                return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PoemListView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request, style = None, sentiment = None, number = 10):
        try:
            poems = Poem.objects.all().filter(author="Machine")
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
                poems = Poem.objects.filter(author="Machine").exclude(input__style="Lorem Ipsum")
                correct = "Machine"

            else:
                poems = Poem.objects.filter(author="Shakespeare") | Poem.objects.filter(author="Ginsberg") | Poem.objects.filter(author="Cummings")
                correct = "Human"

            coin_toss = random.randint(0, 1)
            result = {}

            poem = random.choice(poems)
            
            result['id'] = poem.id
            lines = poem.text.split('\n')
            lines_formatted = [line for line in lines if len(line.strip()) > 10]

            text = random.choice(lines_formatted).strip()
            result['text'] = text

            result["correct"] = correct

            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)



class StatisticsView(views.APIView):
    
    permission_classes = (AllowAny,)

    def get(self, request: Request):

            result = {}

            result['cummings_words'], result['cummings_counts'] = statisticsHelper.generate_word_count_from_file('cummings.txt')
            result['generated_cummings_words'], result['generated_cummings_counts'] = statisticsHelper.generate_word_count_from_file('generated_cummings.txt')
            result['shakespeare_words'], result['shakespeare_counts'] = statisticsHelper.generate_word_count_from_file('shakespeare_sonnets.txt')
            result['generated_shakespeare_words'], result['generated_shakespeare_counts'] = statisticsHelper.generate_word_count_from_file('generated_shakespeare.txt')
            result['ginsberg_words'], result['ginsberg_counts'] = statisticsHelper.generate_word_count_from_file('ginsberg.txt')
            result['generated_ginsberg_words'], result['generated_ginsberg_counts'] = statisticsHelper.generate_word_count_from_file('generated_ginsberg.txt')

            try:
                return Response(result, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)

class GenerationsCount(views.APIView):
    
    permission_classes = (AllowAny,)

    def get(self, request: Request):
        try:
            Input.objects.count()
            coin_toss = random.randint(0, 1)
            result = {"count": Input.objects.count()}

            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)