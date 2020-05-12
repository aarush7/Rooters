from rest_framework.generics import ListCreateAPIView,GenericAPIView,RetrieveUpdateDestroyAPIView
from user_roles.models import operator 
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from user_roles.Serializers.OperatorSerializers import OperatorListSerializer,OperatorEditSerializer
class OperatorView(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = operator.objects.all()
    serializer_class = OperatorListSerializer

    def perform_create(self, serializer):
        
        return serializer.save()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class OperatorupdateView(RetrieveUpdateDestroyAPIView):
    queryset = operator.objects.all()
    serializer_class = OperatorEditSerializer