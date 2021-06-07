from django.urls import path

from .views import *

app_name = 'backend'

urlpatterns = [
    path('', test, name='test'),
    path('generate/', GeneratePoemView.as_view(), name='generate'),
    path('save/', SavePoem.as_view(), name='save'),
    path('poems/<int:id>/', PoemView.as_view(), name='poem'),
    path('poems/', PoemListView.as_view(), name='poems'),
    path('poems/style=<style>/', PoemListView.as_view(), name='poems'),
    path('poems/sentiment=<sentiment>/', PoemListView.as_view(), name='poems'),
    path('poems/style=<style>&sentiment=<sentiment>/', PoemListView.as_view(), name='poems'),
    path('rating/', RatingView.as_view(), name='rating'),
    path('rating/<int:id>/', RatingView.as_view(), name='rating'),
    path('add/rate/<int:id>/', CreateRate.as_view(), name='rate'),
    path('add/turing-test-vote/<int:id>/', CreateTuringTestVote.as_view(), name='TTvote'),
    path('get/tt-fragment/', TuringTestFragmentView.as_view(), name='tt-fragment')
]