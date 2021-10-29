import io
import csv
import pandas as pd
from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from geocoding.models import Task
from geocoding.serializers import FileUploadSerializer, SaveFileSerializer
from geocoding.utils import get_address, get_distance

# we can send response with help of Response when we've created Task or model
# what we need to display when we're in the API
# just requst to API and get json back


#class File(models.Model):
#    id = models.CharField(primary_key=True, max_length=6)
#    staff_name = models.CharField(max_length=100)
#    position = models.CharField(max_length=200)
#    age = models.IntegerField()
#    year_joined = models.CharField(max_length=4)
#
#    def __str__(self):
#        return self.staff_name


#class TaskView(APIView):
#    def get(self, request):
#        """
#        Need to modify for getting a specific response
#        """
#        tasks = Task.objects.all()
#        serializer = TaskSerializer(tasks, many=True)
#        return Response(serializer.data)
#
#    def post(self):
#        pass


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        myfile = serializer.validated_data['myfile']
        reader = pd.read_csv(myfile)
        print("***")
        print(myfile)
        return Response({'Hi there': "complete"})
