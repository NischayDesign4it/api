from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, request
from .models import temphum, Status
from .serializer import TempHumSerializer, StatusSerializer


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



class StatusPost(APIView):
    def post(self, request):
        # Ensure there's only one Status instance
        instance, created = Status.objects.get_or_create(id=3)  # Assuming there should only be one instance with ID 1

        serializer = StatusSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Ensure there's only one Status instance
        instance = Status.objects.first()
        if instance is None:
            return Response({"detail": "No status entry found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = StatusSerializer(instance)
        return Response(serializer.data)