from django.urls import path

from .views import *

app_name = 'backend'

urlpatterns = [
    path('', test, name='test'),
    path('generate/', GeneratePoemView.as_view(), name='generate'),
    path('generate-line/', GeneratePoemLineView.as_view(), name='generate-line'),
    path('generate-style-transfer/', GenerateStyleTransferView.as_view(), name='generate-style-transfer'),
    path('save/', SavePoem.as_view(), name='save'),
    path('poems/<int:id>/', PoemView.as_view(), name='poem'),
    path('poems/', PoemListView.as_view(), name='poems'),
    path('poems/style=<style>/', PoemListView.as_view(), name='poems'),
    path('poems/sentiment=<sentiment>/', PoemListView.as_view(), name='poems'),
    path('poems/style=<style>&sentiment=<sentiment>/', PoemListView.as_view(), name='poems'),
    path('rating/', RatingView.as_view(), name='rating'),
    path('rating/<int:id>/', RatingView.as_view(), name='rating'),
    path('add/rate/<int:id>/', CreateRate.as_view(), name='rate'),
    path('sentiment/<int:id>/', JSONSentimentView.as_view(), name='sentiment'),
    path('add/turing-test-vote/<int:id>/', CreateTuringTestVote.as_view(), name='TTvote'),
    path('sentiment-analysis/', SentimentAnalysisView.as_view(), name='sentiment-analysis'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
    path('get/tt-fragment/', TuringTestFragmentView.as_view(), name='tt-fragment'),
    path('generations-count/', GenerationsCount.as_view(), name='generations-count')
]