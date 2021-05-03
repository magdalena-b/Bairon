from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from django.core.serializers import serialize, json
from django.forms.models import model_to_dict

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
        serializer = PoemSerializer(data=request.data)
        if serializer.is_valid():
            created = serializer.create(serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)