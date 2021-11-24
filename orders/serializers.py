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
    OrderDetails,
    TrackingStatus,
    OrderItems,
    PaymentDetails,
    UserPayments,


)


class OrderDetailsSerializer(ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = "__all__"




class TrackingStatusSerializer(ModelSerializer):
    class Meta:
        model = TrackingStatus
        fields = "__all__"




class OrderItemsSerializer(ModelSerializer):
    class Meta:
        model = OrderItems
        fields = "__all__"



class PaymentDetailsSerializer(ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = "__all__"



class UserPaymentsSerializer(ModelSerializer):
    class Meta:
        model = UserPayments
        fields = "__all__"




