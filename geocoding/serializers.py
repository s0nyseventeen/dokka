from rest_framework import serializers
from .models import Task


class FileUploadSerializer(serializers.Serializer):
    myfile = serializers.FileField()


class SaveFileSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = '__all__'
#        fields = (
#            #'task_id',  # need them when upload file?
#            #'status',   
#            'point',
#            'latitude',
#            'longitude'  # to show in response?
#        )
