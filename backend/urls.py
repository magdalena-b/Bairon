from django.urls import path

from .views import *

app_name = 'backend'

urlpatterns = [
    path('', test, name='test'),
    path('generate/', GeneratePoemView.as_view(), name='generate'),
    path('save/', SavePoem.as_view(), name='save'),
]