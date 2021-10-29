from django.urls import path
from geocoding.views import UploadFileView

urlpatterns = [
    path('calculateDistances/', UploadFileView.as_view()),
]
