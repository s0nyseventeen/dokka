from django.urls import path
from geocoding.views import TaskView

urlpatterns = [
    path('calculateDistances/', TaskView.as_view()),
]
