from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Rate
from .serializers import RateSerializer


class RateAPIView(ListAPIView):
    queryset = Rate.objects.select_related("currency")
    serializer_class = RateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date"]
