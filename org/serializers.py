from rest_framework import serializers
from .models import Position, Worker

class WorkerSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=200)

class PositionSerializer(serializers.ModelSerializer):
    workers = serializers.SerializerMethodField('get_worker_names')

    class Meta:
        model = Position
        fields = ('title', 'workers')


    def get_worker_names(self, obj):
        names = [worker.full_name for worker in obj.workers.all()]
        return names




