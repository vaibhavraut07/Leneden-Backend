from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Game(models.Model):
    player1 = models.ForeignKey(User, related_name='games_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(User, related_name='games_as_player2', on_delete=models.CASCADE)
    winner = models.ForeignKey(User, related_name='games_won', on_delete=models.CASCADE, null=True, blank=True)
    is_draw = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Move(models.Model):
    game = models.ForeignKey(Game, related_name='moves', on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)