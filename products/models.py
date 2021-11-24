from django.db import models

# Create your models here.
from LightCart.models import BaseModel

class Products(BaseModel):
    product_name = models.CharField(max_length=30)
    product_price = models.FloatField(max_length=20)
    image_id = models.ForeignKey("products.ProductImages" , on_delete=models.DO_NOTHING)
    product_short_desc = models.CharField(max_length=100, null=True)
    product_long_desc = models.TextField(null=True, blank=True)
    product_benefits = models.TextField(null=True)
    product_about_it = models.TextField(null=True)
    discount_id = models.ForeignKey("products.Discount", on_delete=models.DO_NOTHING,null=True)
    category_id = models.ForeignKey("products.ProductCategory", on_delete=models.DO_NOTHING)
    brand = models.ForeignKey("products.Brand",on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_name


class Brand(BaseModel):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class ProductCategory(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    deleted_datetime = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Discount(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    discount_percent = models.DecimalField(decimal_places=2, max_digits=10)
    deleted_datetime = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    price = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class ProductStock(BaseModel):
    product_id = models.ForeignKey("products.Products", on_delete=models.DO_NOTHING)
    category_id = models.ForeignKey("products.ProductCategory", on_delete=models.DO_NOTHING)
    is_stock_availability = models.BooleanField(default=True)


class ProductOptions(BaseModel):
     product_opt_name = models.CharField(max_length=20)
     product_id = models.ForeignKey("products.Products", on_delete=models.DO_NOTHING)
     discount_id = models.ForeignKey("products.Discount", on_delete=models.DO_NOTHING)
     price = models.CharField(max_length=200, null=True)
     deleted_datetime = models.DateTimeField(auto_now_add=True)


class Combos(BaseModel):
    product_combo = models.CharField(max_length=20,default=None)
    product_id = models.ForeignKey("products.Products", on_delete=models.DO_NOTHING)
    discount_id = models.ForeignKey("products.Discount", on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    price = models.CharField(max_length=200, null=True)


class ProductReviews(BaseModel):
    product_id = models.ForeignKey("products.Products", on_delete=models.DO_NOTHING)
    category_id = models.ForeignKey("products.ProductCategory", on_delete=models.DO_NOTHING)
    massage = models.TextField()


class ProductImages(BaseModel):
    product_image = models.ImageField(upload_to="product_pic",null=True, default=None)
    description = models.TextField(null=True)
    deleted_datetime = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Slider(BaseModel):
    slider_name = models.CharField(max_length=20)
    slider_image = models.ImageField(upload_to="slider_pic", null=True, default=None)
    description = models.TextField(null=True)
    deleted_datetime = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


