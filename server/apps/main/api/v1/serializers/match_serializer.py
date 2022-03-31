from rest_framework import serializers
from rest_framework.fields import HiddenField
from rest_framework.serializers import ModelSerializer, ValidationError
from server.apps.main.models import Match


class MatchSerializer(ModelSerializer):
    sender = HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        if data['sender'] == self.context['recipient']:
            raise ValidationError('you cannot share your sympathy to yourself.')
        return data

    def create(self, validated_data):
        return Match.objects.create(sender=validated_data['sender'], recipient=self.context['recipient'])

    class Meta:
        model = Match
        fields = ['sender']
