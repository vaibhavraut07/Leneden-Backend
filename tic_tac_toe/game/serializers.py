from rest_framework import serializers
from .models import User, Game, Move

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
# Move Serializer
class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ['id', 'game', 'player', 'position', 'symbol', 'created_at']
        extra_kwargs = {
            'player': {'read_only': True},  # Automatically set to the logged-in user
            'symbol': {'read_only': True},  # Automatically set based on the player
        }

# Game Serializer
class GameSerializer(serializers.ModelSerializer):
    moves = MoveSerializer(many=True, read_only=True)
    game_board = serializers.SerializerMethodField()  # Add this field

    class Meta:
        model = Game
        fields = ['id', 'player1', 'player2', 'winner', 'is_draw', 'created_at', 'moves', 'game_board']
        extra_kwargs = {
            'player1': {'read_only': True},  # player1 is automatically set to the logged-in user
            'player2': {'required': True},   # player2 is required but provided in the request
        }

    def get_game_board(self, obj):
        # Initialize an empty 3x3 board
        board = [[' ' for _ in range(3)] for _ in range(3)]

        # Populate the board with moves
        for move in obj.moves.all():
            row = move.position // 3
            col = move.position % 3
            board[row][col] = move.symbol

        # Convert the board to a string representation
        board_str = "\n".join([" | ".join(row) for row in board])
        return board_str