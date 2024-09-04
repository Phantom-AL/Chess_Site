from django.urls import path
from .views import index, players, rules, chessboard, maintaining_the_party

urlpatterns = [
    path('', index, name='index'),
    path('players/', players, name='players'),
    path('rules/', rules, name='rules'),
    path('chessboard/', chessboard, name='chessboard'),
    path('maintaining/', maintaining_the_party, name='maintaining'),
    # концертация юрл в числа, чтобы обеспечить легкость кода
]
