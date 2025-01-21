from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    GameListCreateView,
    GameRetrieveView,
    MoveCreateView,
    UserGameHistoryView
)

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    # Game Endpoints
    path('games/', GameListCreateView.as_view(), name='game-list-create'),
    path('games/<int:pk>/', GameRetrieveView.as_view(), name='game-retrieve'),
    path('moves/', MoveCreateView.as_view(), name='move-create'),

    # Game History
    path('history/', UserGameHistoryView.as_view(), name='user-game-history'),
]