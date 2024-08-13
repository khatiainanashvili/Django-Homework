from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Birds
from .serializesr import BirdSerializer

@api_view(['GET'])
def get_routes(request): 

    routes = [
        "GET /api",
        "GET /api/birds",
        "GET /api/bird/:id"
    ]
    return Response(routes)


@api_view(['GET'])
def get_birds(request):
    birds = Birds.objects.all()
    serializer = BirdSerializer(birds, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_bird(request, id):
   bird = Birds.objects.get(id=id)
   serializer = BirdSerializer(bird, many=False)
   return Response(serializer.data)