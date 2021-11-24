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
from products.models import (
    Products,
    ProductCategory,
    Discount,
    ProductStock,
    ProductOptions,
    Brand,
    Slider,
    ProductImages,
    ProductReviews,
    Combos




)


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"




class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"




class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"



class ProductStockSerializer(ModelSerializer):
    class Meta:
        model = ProductStock
        fields = "__all__"




class ProductOptionsSerializer(ModelSerializer):
    class Meta:
        model = ProductOptions
        fields = "__all__"


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"



class SliderSerializer(ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"



class ProductImagesSerializer(ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "__all__"



class ProductReviewsSerializer(ModelSerializer):
    class Meta:
        model = ProductReviews
        fields = "__all__"


class CombosSerializer(ModelSerializer):
    class Meta:
        model = Combos
        fields = "__all__"

