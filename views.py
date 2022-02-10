from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.



class Home(APIView):

    def get(self, request):
        xabar = {'message': "Hello World!"}
        return JsonResponse(xabar)

    def post(self, request):
        xabar = {'message': "Massage successful done!"}
        return JsonResponse(xabar)

class MovieAPI(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = ModelSerializer


class ActorAPI(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        ser = ActorSerializer(actors, many=True)
        return Response(ser.data)

    def post(self, request):
        actor = request.data
        ser = ActorSerializer(actor)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
    def delete(self, response, pk):
        actor = Actor.objects.get(id=pk)
        actor.delete()
        return JsonResponse({'xabar': "Actor who will givwe is success deleted!"})
    def put(self, request, pk):
        actor = Actor.objects.get(id=pk)
        ser = ActorSerializer(actor, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.deta)
        return JsonResponse({"xabar": "Changing can't be updated!"})