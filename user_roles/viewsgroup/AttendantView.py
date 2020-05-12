from rest_framework.generics import ListCreateAPIView,GenericAPIView,RetrieveUpdateDestroyAPIView
from user_roles.models import attendant 
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from user_roles.Serializers.AttendantSerializers import AttendantListSerializer,AttendantEditSerializer
class AttendantView(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = attendant.objects.all()
    serializer_class = AttendantListSerializer

    def perform_create(self, serializer):
        
        return serializer.save()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class AttendantupdateView(RetrieveUpdateDestroyAPIView):
    queryset = attendant.objects.all()
    serializer_class = AttendantEditSerializer