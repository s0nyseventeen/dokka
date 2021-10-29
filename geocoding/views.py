from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geocoding.models import Task
from geocoding.serializers import TaskSerializer

# we can send response with help of Response when we've created Task or model
# what we need to display when we're in the API
# just requst to API and get json back


class TaskView(APIView):
    def get(self, request):
        """
        Need to modify for getting a specific response
        """
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self):
        pass
