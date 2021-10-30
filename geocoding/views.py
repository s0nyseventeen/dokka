import pandas as pd
from itertools import combinations
from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from geocoding.models import Task, Point
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


#class Task(models.Model):
#    point = models.CharField(max_length=255)
#    latitude = models.FloatField()
#    longitude = models.FloatField()
#    status = models.BooleanField()  # (running, done)
#    task_id = models.UUIDField(default=uuid.uuid4)
#    address = models.CharField(max_length=255)
#    distance = models.FloatField()
#
#    def __str__(self):
#        return self.task_id



class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
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

        
        print(d)



        return Response(
            {
                'task_id': task_obj.task_id,
                'status': task_obj.status
            }
        )  # !!! need to be task_id, status



# need to implement logic to save point and its coordinates (tuple)
# create dict to save there 
# calculation
# save to db