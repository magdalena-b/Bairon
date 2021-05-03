from django.urls import path

from backend.views import test

app_name = 'backend'

urlpatterns = [
    path('', test, name='test'),
]