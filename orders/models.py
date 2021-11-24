from django.db import models

from LightCart.models import BaseModel



class UserPayments(BaseModel):
    user_id = models.ForeignKey("authentication.User",on_delete=models.DO_NOTHING)
    payment_type = models.CharField(max_length=100,null=True,default=True)
    account_no = models.BigIntegerField(null=True)


class CartItems(BaseModel):
    product_id = models.ForeignKey("products.Products", on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=None)
    user_id = models.ForeignKey("authentication.User", on_delete=models.DO_NOTHING)


class OrderItems(BaseModel):
    order_id = models.ForeignKey("orders.OrderDetails", on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey("products.Products", on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=None)


class OrderDetails(BaseModel):
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    user_id = models.ForeignKey("authentication.User", on_delete=models.DO_NOTHING)
    payment_id = models.ForeignKey("orders.PaymentDetails", on_delete=models.DO_NOTHING)


class PaymentDetails(BaseModel):
    order_id = models.ForeignKey("orders.OrderDetails", on_delete=models.DO_NOTHING)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=20,default=None,null=True)


class TrackingStatus(BaseModel):
    user_id = models.ForeignKey("authentication.User", on_delete=models.DO_NOTHING)
    payment_id = models.ForeignKey("orders.PaymentDetails", on_delete=models.DO_NOTHING)
    order_id = models.ForeignKey("orders.OrderDetails", on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey("products.Products", on_delete=models.DO_NOTHING)



# Create your models here.

