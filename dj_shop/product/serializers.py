from rest_framework import serializers

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "category_slug", "ctype", "slug", "description",
                  "price", "discount_price", "tip", "get_image",
                  "get_thumbnail")


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "ctype",
            "get_absolute_url",
            "products",
        )