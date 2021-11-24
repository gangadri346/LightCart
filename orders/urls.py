from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
from LightCart.views import LightCartViewSet
from .views import (
    OrderDetailsViewSet,
    TrackingStatusViewSet,
    OrderItemsViewSet,
    PaymentDetailsViewSet,
    UserPaymentsViewSet,
                     )


router.register(r"orderdetails", OrderDetailsViewSet, basename="orderdetails")
router.register(r"trackingstatus", TrackingStatusViewSet, basename="trackingstatus")
router.register(r"orderitems", OrderItemsViewSet, basename="orderitems")
router.register(r"paymentdetails", PaymentDetailsViewSet, basename="paymentdetails")
router.register(r"userpayments", UserPaymentsViewSet, basename="userpayments")
router.register(r"lightkart", LightCartViewSet, basename="lightkart")





urlpatterns = [
    path("", include(router.urls)),
]