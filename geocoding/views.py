import pandas as pd
from itertools import combinations
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import viewsets
from geocoding.models import Task, Point, Link
from geocoding.serializers import (FileUploadSerializer, TaskSerializer,
                                   PointSerializer, LinkSerializer)
from geocoding.utils import get_address, get_distance

# we can send response with help of Response when we've created Task or model
# what we need to display when we're in the API
# just requst to API and get json back


class TaskApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer  # we recieve csv file
    
    def post(self, request, *args, **kwargs):
        d = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        myfile = serializer.validated_data['myfile']
        reader = pd.read_csv(myfile)  # probably can use in func
        task_obj = Task.objects.create()
        for _, row in reader.iterrows():
            new_point_item = Point.objects.create(
                task_id=task_obj, 
                name=row['point'],
                address=get_address(row['latitude'], row['longitude'])
            )
            d[row['point']] = (row['latitude'], row['longitude'])
        d = get_distance(d)
        for k, v in d.items():
            new_link_item = Link.objects.create(
                task_id=task_obj,
                name=k,
                distance=d[k]
            )
        return Response(
            {
                'task_id': task_obj.task_id,
                'status': 'running'
            }
        )
