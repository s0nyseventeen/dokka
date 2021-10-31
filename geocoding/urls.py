from django.urls import path
from geocoding.views import UploadFileView, TaskApiView

urlpatterns = [
    path('calculateDistances/', UploadFileView.as_view()),
    path('getResult/', TaskApiView.as_view()),
]
