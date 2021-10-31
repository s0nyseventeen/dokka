from django.urls import path, include
from rest_framework.routers import DefaultRouter
from geocoding.views import UploadFileView, TaskApiView 

#router = DefaultRouter()
#router.register('Task', TaskApiView)
#router.register('Point', PointApiView)
#router.register('Link', LinkApiView)

urlpatterns = [
    path('calculateDistances/', UploadFileView.as_view()),
    #path('getResult/', include(router.urls)),
    path('getResult/', TaskApiView.as_view()),
]
