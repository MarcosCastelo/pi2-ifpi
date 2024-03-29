from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer

@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return Response(games_serializer.data)

    elif request.method == 'POST':
        game_serializer = GameSerializer(data=request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(
                game_serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            game_serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return Response(game_serializer.data)

    if request.method == 'PUT':
        game_serializer = GameSerializer(game)
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(
                game_serializer.data,
                status = status.HTTP_202_ACCEPTED
            )
        return Response(
            status= status.HTTP_400_BAD_REQUEST
        )
    
    if request.method == 'DELETE':
        game.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


