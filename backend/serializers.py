from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import *


class InputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Input
        fields = ('style', 'first_line', 'model_type')

    def create(self, validated_data):
        try:
            input = Input.objects.create(
                style = validated_data["style"],
                first_line = validated_data["first_line"],
                model_type = validated_data["model_type"]
            )
            input.save()
            return input
        except Exception as e:
            print(e)
        return None


class PoemSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='get_author_display')

    class Meta:
        model = Poem
        fields = '__all__'

    def create(self, validated_data):
        try:
            input, created = Poem.objects.get_or_create(
                id = validated_data["input"].id + 2000,
                author = validated_data.get("get_author_display", "Machine"),
                input = validated_data["input"],
                text = validated_data["text"][:1000],
                generator_type = validated_data["generator_type"],
                style_transfer = validated_data["style_transfer"],
                translations = validated_data["translations"],
                bleu_score = validated_data["bleu_score"],
                sentiment = validated_data["sentiment"],
            )
            input.save()
            return input
        except Exception as e:
            print(e)
            pass
        return None


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'

    def create(self, validated_data):
        try:
            if validated_data["rate"] < 0 or validated_data["rate"] > 10 : raise Exception("rate not in range [0,10]")
            rate, created = Rate.objects.create(
                poem = validated_data["poem"],
                rate = validated_data["rate"],
                category = validated_data["category"],
            )
            rate.save()
            return rate

        except Exception as e:
            print(e)
        return None


class TuringTestVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuringTestVote
        fields = '__all__'

    def create(self, validated_data):
        try:
            ttv, created = TuringTestVote.objects.create(
                poem = validated_data["poem"],
                fragment = validated_data["fragment"],
                vote = validated_data["vote"],
            )
            ttv.save()
            return ttv
        except Exception as e:
            print(e)
        return None
