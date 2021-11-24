from django.db import transaction
from django.db.utils import DatabaseError
from rest_framework import status, viewsets
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from orders.models import CartItems
from .serializers import CartItemsSerializer

class LightCartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer
