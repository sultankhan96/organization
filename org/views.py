from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Worker, Position
from .serializers import WorkerSerializer, PositionSerializer


class WorkerView(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response({"workers": serializer.data})


class PositionView(APIView):
    def get(self, request):
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return Response({"positions": serializer.data})
