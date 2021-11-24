from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
from .views import (
    ProductsViewSet,
    ProductCategoryViewSet,
    DiscountViewSet,
    ProductStockViewSet,
    ProductOptionsViewSet,
    BrandViewSet,
    SliderViewSet,
    ProductImagesViewSet,
    ProductReviewsViewSet,
    CombosViewSet

)





router.register(r"products", ProductsViewSet, basename="products")
router.register(r"productcategory", ProductCategoryViewSet, basename="productcategory")
router.register(r"discount", DiscountViewSet, basename="discount")
router.register(r"productstock", ProductStockViewSet, basename="productstock")
router.register(r"productoptions", ProductOptionsViewSet, basename="productoptions")
router.register(r"brand", BrandViewSet, basename="brand")
router.register(r"slider", SliderViewSet, basename="slider")
router.register(r"productimages", ProductImagesViewSet, basename="productimages")
router.register(r"productreviews", ProductReviewsViewSet, basename="productreviews")
router.register(r" combos", CombosViewSet, basename=" combos")


urlpatterns = [
    path("", include(router.urls)),
]