from rest_framework.generics import ListCreateAPIView,GenericAPIView,RetrieveUpdateDestroyAPIView
from user_roles.models import driver 
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from user_roles.Serializers.DriverSerializers import DriverListSerializer,DriverEditSerializer
class DriverView(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = driver.objects.all()
    serializer_class = DriverListSerializer

    def perform_create(self, serializer):
        
        return serializer.save()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class DriverupdateView(RetrieveUpdateDestroyAPIView):
    queryset = driver.objects.all()
    serializer_class = DriverEditSerializer