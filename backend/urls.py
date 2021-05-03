from django.urls import path

from .views import *

app_name = 'backend'

urlpatterns = [
    path('', test, name='test'),
    path('generate/', GeneratePoemView.as_view(), name='generate'),
    path('save/', SavePoem.as_view(), name='save'),
    path('poem/<int:id>/', PoemView.as_view(), name='poem'),
    path('poems/', PoemListView.as_view(), name='poem'),
    path('poems/style=<style>/', PoemListView.as_view(), name='poem'),
    path('poems/sentiment=<sentiment>/', PoemListView.as_view(), name='poem'),
    path('poems/style=<style>&sentiment=<sentiment>/', PoemListView.as_view(), name='poem'),
]