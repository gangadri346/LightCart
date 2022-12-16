from django.shortcuts import render
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

from orders.models import ( UserPayments,
                            PaymentDetails,
                            OrderItems,
                            TrackingStatus,
                            OrderDetails )



from .serializers import (OrderDetailsSerializer,
                          TrackingStatusSerializer,
                          OrderItemsSerializer,
                          PaymentDetailsSerializer,
                          UserPaymentsSerializer,
                          )

class OrderDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer


class TrackingStatusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset =  TrackingStatus.objects.all()
    serializer_class = TrackingStatusSerializer


class OrderItemsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer


"*****************************************Gangadri*************************************************************"



class PaymentDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailsSerializer


class UserPaymentsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserPayments.objects.all()
    serializer_class = UserPaymentsSerializer





# Create your views here.
