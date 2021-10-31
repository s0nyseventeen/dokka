from rest_framework import serializers
from geocoding.models import Point, Link, Task


class FileUploadSerializer(serializers.Serializer):
    myfile = serializers.FileField()


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = 'name', 'address'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = 'name', 'distance'


class TaskSerializer(serializers.ModelSerializer):
    points = PointSerializer(read_only=True, many=True)
    links = LinkSerializer(read_only=True, many=True) 

    class Meta:
        model = Task
        fields = 'task_id', 'status', 'points', 'links'
