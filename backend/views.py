from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST', ])
def test(request: Request) -> Response:
    return Response({"status": "ok"}, status=status.HTTP_200_OK)