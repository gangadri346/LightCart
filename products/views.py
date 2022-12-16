from django.shortcuts import render

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

from orders.models import CartItems

from products.models import (
    Brand,
    Products,
    ProductCategory,
    Discount,
    ProductStock,
    ProductOptions,
    Slider,
    ProductImages,
    ProductReviews,
    Combos
)

from .serializers import (ProductsSerializer,
                          ProductCategorySerializer,
                          DiscountSerializer,
                          ProductStockSerializer,
                          ProductOptionsSerializer,
                          BrandSerializer,
                          SliderSerializer,
                          ProductImagesSerializer,
                          ProductReviewsSerializer,
                          CombosSerializer)


class ProductsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

"****************************************************************************************************"

    def retrieve(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class DiscountViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class ProductStockViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer


class ProductOptionsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductOptions.objects.all()
    serializer_class = ProductOptionsSerializer


class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


# Create your views here.
class SliderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class ProductImagesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesSerializer


class ProductReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductReviews.objects.all()
    serializer_class = ProductReviewsSerializer


class CombosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]  # permissions are done by me 
    queryset = Combos.objects.all()
    serializer_class = CombosSerializer
