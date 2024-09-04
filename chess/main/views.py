from django.shortcuts import render
from .models import Players


def index(request):
    return render(request, 'index.html')


def players(request):
    players = Players.objects.all()
    return render(request, 'players.html', context={'players': players})


def rules(request):
    return render(request, 'base_rules.html')


def chessboard(request):
    return render(request, 'the_chessboard.html')


def maintaining_the_party(request):
    return render(request, 'maintaining_the_party.html')

