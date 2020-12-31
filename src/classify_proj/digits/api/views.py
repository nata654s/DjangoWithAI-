from rest_framework import viewsets
from ..models import Digits
from .serializers import DigitSerializers


class DigitViewSet(viewsets.ModelViewSet):
    serializer_class = DigitSerializers
    queryset = Digits.objects.all()