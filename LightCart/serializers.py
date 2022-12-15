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
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from authentication.models import User
from orders.models import (
    CartItems
)


class CartItemsSerializer(ModelSerializer): # changes are made
    class Meta:
        model = CartItems
        fields = "__all__"
