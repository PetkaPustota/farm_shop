from rest_framework.generics import CreateAPIView
from order.models import Orders
from order.serializers import OrderCreateSerializer


class OrderView(CreateAPIView):
    queryset = Orders.objects.prefetch_related()
    serializer_class = OrderCreateSerializer
