from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import GasStationCompany, GasStation
from .serializers import GasStationCompanyDetailSerializer, GasStationCompanySerializer, GasStationSerializer

# Create your views here.
class GasStationCompanyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = GasStationCompany.objects.all()
    serializer_class = GasStationCompanySerializer
    permission_classes = (AllowAny,)
    permission_classes_by_action = {"create": [IsAuthenticated]}

    def get_permissions(self):
        if self.action in self.permission_classes_by_action:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        return [permission() for permission in self.permission_classes]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GasStationCompanyDetailSerializer(instance)
        return Response(serializer.data)


class GasStationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = GasStation.objects.all()
    serializer_class = GasStationSerializer
    permission_classes = (AllowAny,)
    permission_classes_by_action = {"create": [IsAuthenticated]}

    def get_permissions(self):
        if self.action in self.permission_classes_by_action:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        return [permission() for permission in self.permission_classes]

    @action(detail=False, methods=['get'], url_path='city/(?P<city>[^/.]+)')
    def list_by_city(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(city__slug=kwargs['city'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
