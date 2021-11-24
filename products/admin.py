from django.contrib import admin

# Register your models here.
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


admin.site.register(Brand)
admin.site.register(Products)
admin.site.register(ProductCategory)
admin.site.register(Discount)
admin.site.register(ProductStock)
admin.site.register(ProductOptions)
admin.site.register(Slider)
admin.site.register(ProductImages)
admin.site.register(ProductReviews)
admin.site.register(Combos)


