from app.models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from volontyor.settings import BASE_URL


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = f"{BASE_URL}{instance.image.url}"
        return representation


class VolunteerSerializer(ModelSerializer):
    class Meta:
        model = Volunteer
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = f"{BASE_URL}{instance.image.url}"
        return representation


class InvestorSerializer(ModelSerializer):
    class Meta:
        model = Investor
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = f"{BASE_URL}{instance.image.url}"
        return representation


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = f"{BASE_URL}{instance.image.url}"
        return representation
