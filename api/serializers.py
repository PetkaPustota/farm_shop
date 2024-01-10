from rest_framework import serializers
from api.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'