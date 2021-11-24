from django.contrib import admin
from orders.models import ( UserPayments,
                            PaymentDetails,
                            OrderItems,
                            TrackingStatus,
                            OrderDetails,
                            CartItems)
# Register your models here.
admin.site.register(OrderItems)
admin.site.register(OrderDetails)
admin.site.register(CartItems)
admin.site.register(TrackingStatus)
admin.site.register(PaymentDetails)
admin.site.register(UserPayments)