import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from geocoding.models import Task, Point, Link
from geocoding.serializers import FileUploadSerializer, TaskSerializer
from geocoding.utils import get_address, get_distance


class TaskApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer  # we receive a .csv file

    def post(self, request, *args, **kwargs):
        d = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        myfile = serializer.validated_data['myfile']
        reader = pd.read_csv(myfile)
        task_obj = Task.objects.create()
        for _, row in reader.iterrows():
            Point.objects.create(
                task_id=task_obj,
                name=row['point'],
                address=get_address(row['latitude'], row['longitude'])
            )
            d[row['point']] = (row['latitude'], row['longitude'])
        d = get_distance(d)
        for k, v in d.items():
            Link.objects.create(
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
