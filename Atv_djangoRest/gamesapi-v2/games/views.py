from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse
from .models import *
from .serializers import *


class ApiRoot(generics.GenericAPIView):
	name = 'api-root'

	def get(self, request, *args, **kwargs):
		return Response({
			'players' : reverse(PlayerList.name, request=request),
			'game_categorys' : reverse(GameCategoryList.name, request=request),
			'games' : reverse(GameList.name, request=request),
			'scores' : reverse(ScoreList.name, request=request),
		})


class GameCategoryList(generics.ListCreateAPIView):
	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer
	name = 'gamecategory-list'
	
class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer
	name = 'gamecategory-detail'

class GameList(generics.ListCreateAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	name = 'game-list'

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	name = 'game-detail'

class PlayerList(generics.ListCreateAPIView):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	name = 'player-list'

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	name = 'player-detail'

class ScoreList(generics.ListCreateAPIView):
	queryset = Score.objects.all()
	serializer_class = ScoreSerializer
	name = 'score-list'

class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Score.objects.all()
	serializer_class = ScoreSerializer
	name = 'score-detail'