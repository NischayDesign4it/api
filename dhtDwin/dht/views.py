from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import temphum
from .serializer import TempHumSerializer

class TempHumCreateAPIView(APIView):
    def post(self, request):
        serializer = TempHumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TempHumListAPIView(APIView):
    def get(self, request):
        queryset = temphum.objects.all()
        serializer = TempHumSerializer(queryset, many=True)
        return Response(serializer.data)
