from rest_framework import serializers

from order.models import Orders, OrderProducts
from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ['id']


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProducts
        exclude = ['orders', 'id']


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderProductSerializer(many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    class Meta:
        model = Orders
        exclude = ['created_at', "id"]

    def create(self, validated_data):
        order_data = validated_data.pop('items')
        order = Orders.objects.create(**validated_data)

        full_price = 0
        order_items = []
        product_list = []
        quantities_list = []
        order_data = sorted(order_data, key=lambda x: x['product']['id'])

        for item_data in order_data:
            product_list.append(item_data.pop("product")['id'])
            quantities_list.append(item_data.pop("quantity"))
        products = Product.objects.filter(pk__in=product_list).order_by('pk')

        for product, quantity in zip(products, quantities_list):
            full_price += product.price * quantity
            order_items.append(OrderProducts(orders=order, product=product, quantity=quantity))

        OrderProducts.objects.bulk_create(order_items)
        order.total_price = full_price

        return order
