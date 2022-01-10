from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status, views
from rest_framework.decorators import api_view, permission_classes
from django.core.serializers import serialize, json
from django.forms.models import model_to_dict
from rest_framework import serializers
from rest_framework.throttling import AnonRateThrottle

import random
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction 
import json

from .serializers import *
from NLP.statistics_helper import statisticsHelper
from NLP.sentiment_helper import sentimentHelper
import sys
import re
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
                        first_line = input.first_line,
                        model_type = input.model_type
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
                        first_line = input.first_line,
                        model_type = input.model_type
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

                result = {}
                result['translated_lines'] = result_lines
                
                candidates = []
                
                for result_line in result_lines:
                    candidate = result_line.lower()
                    candidate = re.sub(r"[^a-zA-Z]+\s\s+", "", candidate)
                    candidate = candidate.split()
                    reference = line.split()
                    candidates.append(candidate)

                chencherry = SmoothingFunction()
                bleu_score = sentence_bleu(candidates, reference, smoothing_function=chencherry.method1, weights=(0.25, 0.25, 0.25, 0.25))     
        

                result['bleu_score'] = bleu_score

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
        # data["sentiment"] = data.get("sentiment", "normal")
        print(data["generator_type"])

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
                data["translated_lines"] = poem.translations.split("|")
                data["sentiment"] = poem.sentiment
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
                result["rate-average"] = poem.rate_set.filter(category="overall").aggregate(models.Avg('rate'))["rate__avg"]
                result["grammar-rate-average"] = poem.rate_set.filter(category="grammar").aggregate(models.Avg('rate'))["rate__avg"]
                result["style-rate-average"] = poem.rate_set.filter(category="style").aggregate(models.Avg('rate'))["rate__avg"]
                result["style-transfer-rate-average"] = poem.rate_set.filter(category="style_transfer").aggregate(models.Avg('rate'))["rate__avg"]
                result["rate-count"] = len(poem.rate_set.all())
                result["TT-human"] = len(poem.turingtestvote_set.filter(vote="Human"))
                result["TT-machine"] = len(poem.turingtestvote_set.filter(vote="Machine"))
                return Response(result, status=status.HTTP_200_OK)
            else:
                result = {}
                result["rate-average"] = Rate.objects.filter(category="overall").aggregate(models.Avg('rate'))['rate__avg']
                result["style-transfer-rate-average"] = Rate.objects.filter(category="style_transfer").aggregate(models.Avg('rate'))["rate__avg"]
                result["rate-count"] = len(Rate.objects.all())
                result["TT-human"] = len(TuringTestVote.objects.filter(vote="Human"))
                result["TT-machine"] = len(TuringTestVote.objects.filter(vote="Machine"))
                result["TT-TH"] = len(TuringTestVote.objects.filter(vote="Human").exclude(poem__author="Machine"))
                result["TT-FH"] = len(TuringTestVote.objects.filter(vote="Human").filter(poem__author="Machine"))
                result["TT-TM"] = len(TuringTestVote.objects.filter(vote="Machine").filter(poem__author="Machine"))
                result["TT-FM"] = len(TuringTestVote.objects.filter(vote="Machine").exclude(poem__author="Machine"))
                return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PoemListView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request, style = None, sentiment = None, number = 20):
        try:
            poems = Poem.objects.all().filter(author="Machine")
            if style:
                poems = poems.filter(input__style=style)
            if sentiment:
                poems = poems.filter(sentiment=sentiment)
            result = {"all": []}
            for poem in list(poems.order_by('-views'))[:number]:
                result["all"].append({"id": poem.id, "input": poem.input.first_line, "text": poem.text, "style": poem.input.style, "generator_type": poem.generator_type})
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


class JSONSentimentView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request, id):
        try:
            poem = Poem.objects.get(id=id)
            result = {}
            result['json_sentiment'] = json.loads(poem.sentiment)
            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class TuringTestFragmentView(views.APIView):
    
    permission_classes = (AllowAny,)

    def get(self, request: Request, id = None):
        try:
            coin_toss = random.randint(0, 1)
            result = {}

            poems = Poem.objects.none()

            while poems.count() == 0:

                coin_toss = random.randint(0, 1)

                if coin_toss == 0:
                    poems = Poem.objects.filter(author="Machine").filter(model_type="full").exclude(input__style="Lorem Ipsum")
                    correct = "Machine"

                else:
                    poems = Poem.objects.filter(author="Shakespeare") | Poem.objects.filter(author="Whitman") | Poem.objects.filter(author="Cummings")
                    correct = "Human"

            coin_toss = random.randint(0, 1)
            result = {}

            poems = [poem for poem in poems if (poem != "" and  poem != "\n")]


            lines_formatted = []
            
            while lines_formatted == []:
                poem = random.choice(poems)
                result['id'] = poem.id
                lines = poem.text.split('\n')
                lines_formatted = [line for line in lines if len(line.strip()) > 10 and line and line.strip() and line != "\n" and line != " "]


            text = random.choice(lines_formatted).strip()
            while (not (text and text.strip())):
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
            result['generated_cummings_gpt2_words'], result['generated_cummings_gpt2_counts'] = statisticsHelper.generate_word_count_from_db("Cummings", "gpt2")
            result['generated_cummings_gpt_neo_words'], result['generated_cummings_gpt_neo_counts'] = statisticsHelper.generate_word_count_from_db("Cummings", "gpt-neo")

            result['shakespeare_words'], result['shakespeare_counts'] = statisticsHelper.generate_word_count_from_file('shakespeare_sonnets.txt')
            result['generated_shakespeare_gpt2_words'], result['generated_shakespeare_gpt2_counts'] = statisticsHelper.generate_word_count_from_db("Shakespeare", "gpt2")
            result['generated_shakespeare_gpt_neo_words'], result['generated_shakespeare_gpt_neo_counts'] = statisticsHelper.generate_word_count_from_db("Shakespeare", "gpt-neo")

            result['whitman_words'], result['whitman_counts'] = statisticsHelper.generate_word_count_from_file('whitman.txt')
            result['generated_whitman_gpt2_words'], result['generated_whitman_gpt2_counts'] = statisticsHelper.generate_word_count_from_db("Whitman", "gpt2")
            result['generated_whitman_gpt_neo_words'], result['generated_whitman_gpt_neo_counts'] = statisticsHelper.generate_word_count_from_db("Whitman", "gpt-neo")
            

            try:
                return Response(result, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)


class PoetryTuringTestStatisticsView(views.APIView):
    
    permission_classes = (AllowAny,)

    def get(self, request: Request):

            try:

                result = {}
                
                # Whitman

                result["TT-TM-gpt2-whitman"] = len(TuringTestVote.objects.filter(vote="Machine", poem__author="Machine", poem__input__model_type="gpt2", poem__input__style="Whitman"))
                result["TT-TM-gpt-neo-whitman"] = len(TuringTestVote.objects.filter(vote="Machine").filter(poem__author="Machine").filter(poem__input__model_type="gpt-neo").filter(poem__input__style="Whitman"))

                result["TT-FH-gpt2-whitman"] = len(TuringTestVote.objects.filter(vote="Human", poem__author="Machine", poem__input__model_type="gpt2", poem__input__style="Whitman"))
                result["TT-FH-gpt-neo-whitman"] = len(TuringTestVote.objects.filter(vote="Human", poem__author="Machine", poem__input__model_type="gpt-neo", poem__input__style="Whitman"))

                result["TT-TH-whitman"] = len(TuringTestVote.objects.filter(vote="Human").filter(poem__author="Whitman"))
                result["TT-FM-whitman"] = len(TuringTestVote.objects.filter(vote="Machine").filter(poem__author="Whitman"))


                # Cummings

                result["TT-TM-gpt2-cummings"] = len(TuringTestVote.objects.filter(vote="Machine").filter(poem__author="Machine").filter(poem__input__model_type="gpt2").filter(poem__input__style="Cummings"))
                result["TT-TM-gpt-neo-cummings"] = len(TuringTestVote.objects.filter(vote="Machine").filter(poem__author="Machine").filter(poem__input__model_type="gpt-neo").filter(poem__input__style="Cummings"))

                result["TT-FH-gpt2-cummings"] = len(TuringTestVote.objects.filter(vote="Human").filter(poem__author="Machine").filter(poem__input__model_type="gpt2").filter(poem__input__style="Cummings"))
                result["TT-FH-gpt-neo-cummings"] = len(TuringTestVote.objects.filter(vote="Human").filter(poem__author="Machine").filter(poem__input__model_type="gpt-neo").filter(poem__input__style="Cummings"))

                result["TT-TH-cummings"] = len(TuringTestVote.objects.filter(vote="Human").filter(poem__author="Cummings"))
                result["TT-FM-cummings"] = len(TuringTestVote.objects.filter(vote="Machine").filter(poem__author="Cummings"))

                # Shakespeare

                result["TT-TM-gpt2-shakespeare"] = len(TuringTestVote.objects.filter(vote="Machine").filter(poem__author="Machine").filter(poem__input__model_type="gpt2").filter(poem__input__style="Shakespeare"))
                result["TT-TM-gpt-neo-shakespeare"] = len(TuringTestVote.objects.filter(vote="Machine").filter(poem__author="Machine").filter(poem__input__model_type="gpt-neo").filter(poem__input__style="Shakespeare"))

                result["TT-FH-gpt2-shakespeare"] = len(TuringTestVote.objects.filter(vote="Human").filter(poem__author="Machine").filter(poem__input__model_type="gpt2").filter(poem__input__style="Shakespeare"))
                result["TT-FH-gpt-neo-shakespeare"] = len(TuringTestVote.objects.filter(vote="Human").filter(poem__author="Machine").filter(poem__input__model_type="gpt-neo").filter(poem__input__style="Shakespeare"))
                

                result["TT-TH-shakespeare"] = len(TuringTestVote.objects.filter(vote="Human").filter(poem__author="Shakespeare"))
                result["TT-FM-shakespeare"] = len(TuringTestVote.objects.filter(vote="Machine").filter(poem__author="Shakespeare"))

                # Human

                result["TT-TH"] = len(TuringTestVote.objects.filter(vote="Human").exclude(poem__author="Machine"))
                result["TT-FM"] = len(TuringTestVote.objects.filter(vote="Machine").exclude(poem__author="Machine"))


                return Response(result, status=status.HTTP_200_OK)

            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)


class RatingStatisticsView(views.APIView):
    
    permission_classes = (AllowAny,)

    def get(self, request: Request):

            try:

                result = {}

                # cummings

                result["overall-cummings-gpt2"] = Rate.objects.filter(category="overall").filter(poem__input__style="Cummings").filter(poem__input__model_type="gpt2").aggregate(models.Avg('rate'))["rate__avg"]
                result["grammar-cummings-gpt2"] = Rate.objects.filter(category="grammar").filter(poem__input__style="Cummings").filter(poem__input__model_type="gpt2").aggregate(models.Avg('rate'))["rate__avg"]
                result["style-cummings-gpt2"] = Rate.objects.filter(category="style").filter(poem__input__style="Cummings").filter(poem__input__model_type="gpt2").aggregate(models.Avg('rate'))["rate__avg"]

                result["overall-cummings-gpt-neo"] = Rate.objects.filter(category="overall").filter(poem__input__style="Cummings").filter(poem__input__model_type="gpt-neo").aggregate(models.Avg('rate'))["rate__avg"]
                result["grammar-cummings-gpt-neo"] = Rate.objects.filter(category="grammar").filter(poem__input__style="Cummings").filter(poem__input__model_type="gpt-neo").aggregate(models.Avg('rate'))["rate__avg"]
                result["style-cummings-gpt-neo"] = Rate.objects.filter(category="style").filter(poem__input__style="Cummings").filter(poem__input__model_type="gpt-neo").aggregate(models.Avg('rate'))["rate__avg"]


                # shakespeare

                result["overall-shakespeare-gpt2"] = Rate.objects.filter(category="overall").filter(poem__input__style="Shakespeare").filter(poem__input__model_type="gpt2").aggregate(models.Avg('rate'))["rate__avg"]
                result["grammar-shakespeare-gpt2"] = Rate.objects.filter(category="grammar").filter(poem__input__style="Shakespeare").filter(poem__input__model_type="gpt2").aggregate(models.Avg('rate'))["rate__avg"]
                result["style-shakespeare-gpt2"] = Rate.objects.filter(category="style").filter(poem__input__style="Shakespeare").filter(poem__input__model_type="gpt2").aggregate(models.Avg('rate'))["rate__avg"]

                result["overall-shakespeare-gpt-neo"] = Rate.objects.filter(category="overall").filter(poem__input__style="Shakespeare").filter(poem__input__model_type="gpt-neo").aggregate(models.Avg('rate'))["rate__avg"]
                result["grammar-shakespeare-gpt-neo"] = Rate.objects.filter(category="grammar").filter(poem__input__style="Shakespeare").filter(poem__input__model_type="gpt-neo").aggregate(models.Avg('rate'))["rate__avg"]
                result["style-shakespeare-gpt-neo"] = Rate.objects.filter(category="style").filter(poem__input__style="Shakespeare").filter(poem__input__model_type="gpt-neo").aggregate(models.Avg('rate'))["rate__avg"]


                # whitman

                result["overall-whitman-gpt2"] = Rate.objects.filter(category="overall").filter(poem__input__style="Whitman").filter(poem__input__model_type="gpt2").aggregate(models.Avg('rate'))["rate__avg"]
                result["grammar-whitman-gpt2"] = Rate.objects.filter(category="grammar").filter(poem__input__style="Whitman").filter(poem__input__model_type="gpt2").aggregate(models.Avg('rate'))["rate__avg"]
                result["style-whitman-gpt2"] = Rate.objects.filter(category="style").filter(poem__input__style="Whitman").filter(poem__input__model_type="gpt2").aggregate(models.Avg('rate'))["rate__avg"]

                result["overall-whitman-gpt-neo"] = Rate.objects.filter(category="overall").filter(poem__input__style="Whitman").filter(poem__input__model_type="gpt-neo").aggregate(models.Avg('rate'))["rate__avg"]
                result["grammar-whitman-gpt-neo"] = Rate.objects.filter(category="grammar").filter(poem__input__style="Whitman").filter(poem__input__model_type="gpt-neo").aggregate(models.Avg('rate'))["rate__avg"]
                result["style-whitman-gpt-neo"] = Rate.objects.filter(category="style").filter(poem__input__style="Whitman").filter(poem__input__model_type="gpt-neo").aggregate(models.Avg('rate'))["rate__avg"]





                return Response(result, status=status.HTTP_200_OK)

            except Exception as e:
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

class SentimentAnalysisView(views.APIView):

    permission_classes = (AllowAny,)

    def get(self, request: Request):

        result = {}
        f = open("sentiment.json")
        file = json.load(f)
        result['cummings_analysis'] = file['cummings']
        result['shakespeare_analysis'] = file['shakespeare']
        result['whitman_analysis'] = file['whitman']
                    
        result['generated_cummings_analysis'] = file['generated_cummings']
        result['generated_shakespeare_analysis'] = file['generated_shakespeare']
        result['generated_whitman_analysis'] = file['generated_whitman']
        
        try: 
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
