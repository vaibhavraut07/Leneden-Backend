from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Game, Move  # Import the custom User model
from .serializers import UserSerializer, GameSerializer, MoveSerializer

# User Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()  # Use the custom User model
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

# User Login View
class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()  # Use the custom User model
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

# Game List and Create View
class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        player1 = self.request.user  # Logged-in user is player1
        player2_id = self.request.data.get('player2')  # Get player2 ID from request data

        # Ensure player2_id is provided
        if not player2_id:
            raise serializers.ValidationError({"player2": "This field is required."})

        # Fetch player2 from the database
        try:
            player2 = User.objects.get(id=player2_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"player2": "Player not found."})

        # Save the game with player1 and player2
        serializer.save(player1=player1, player2=player2)

# Game Retrieve View
class GameRetrieveView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (permissions.IsAuthenticated,)

# Move Create View
class MoveCreateView(generics.CreateAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        game_id = self.request.data.get('game')
        game = Game.objects.get(id=game_id)
        player = self.request.user
        position = self.request.data.get('position')

        # Check if the move is valid
        if game.winner or game.is_draw:
            return Response({'error': 'Game is already over'}, status=status.HTTP_400_BAD_REQUEST)

        if player != game.player1 and player != game.player2:
            return Response({'error': 'You are not a player in this game'}, status=status.HTTP_400_BAD_REQUEST)

        if game.moves.filter(position=position).exists():
            return Response({'error': 'Position already taken'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(game=game, player=player, position=position)

        # Check for a winner or draw after the move
        self.check_game_status(game)

    def check_game_status(self, game):
        moves = game.moves.all()
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for combo in winning_combinations:
            positions = [move.position for move in moves if move.player == game.player1]
            if all(pos in positions for pos in combo):
                game.winner = game.player1
                game.save()
                return

            positions = [move.position for move in moves if move.player == game.player2]
            if all(pos in positions for pos in combo):
                game.winner = game.player2
                game.save()
                return

        if moves.count() == 9:
            game.is_draw = True
            game.save()

# Game History View
class UserGameHistoryView(generics.ListAPIView):
    serializer_class = GameSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Game.objects.filter(player1=user) | Game.objects.filter(player2=user)