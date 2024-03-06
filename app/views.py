from rest_framework.views import APIView, Response
from rest_framework.generics import get_object_or_404
from .models import * 
from rest_framework import status
from .serializers import *

class ReceptListView(APIView):

    def get(self, request):
        receipes = Receipes.objects.all()
        serializer = ReceptListSerializer(receipes,many = True)
        return Response({"receipes": serializer.data})
    
class ReceptDetailView(APIView):

    def get(self, request, pk):
        recept = Receipes.objects.filter(id=pk).first()
        serializer = ReceptDetailSerializer(recept)
        return Response({"recept": serializer.data})
    
class ReceptUpdateView(APIView):

    def get(self, request, pk):
        recept = Receipes.objects.filter(id=pk).first()
        serializer = ReceptDetailSerializer(recept)
        return Response({"recept": serializer.data})

    def patch(self, request, pk):
        recept = get_object_or_404(Receipes.objects.all(), id = pk)
        serializer = ReceptUpdateSerializer(recept, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class ReceptDeleteView(APIView):

    def get(self, request, pk):
        recept = Receipes.objects.filter(id=pk).first()
        serializer = ReceptDetailSerializer(recept)
        return Response({"recept": serializer.data})

    def delete(self, request, pk):
        recept = get_object_or_404(Receipes.objects.all(), id = pk)
        recept.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReceptCreateView(APIView):
    
    def post(self, request):
        serializer = ReceptCreateSerializer(data = request.data, context = {"request": request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    
        return Response(status=status.HTTP_400_BAD_REQUEST)
