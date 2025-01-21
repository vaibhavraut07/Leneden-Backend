from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Game, Move

# User Serializer for Registration
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Move Serializer
class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ['id', 'game', 'player', 'position', 'created_at']

# Game Serializer
class GameSerializer(serializers.ModelSerializer):
    moves = MoveSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'player1', 'player2', 'winner', 'is_draw', 'created_at', 'moves']