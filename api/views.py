from django.shortcuts import render
from rest_framework import filters, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from api.models import Product
from api.serializers import ProductListSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['brand__name', 'category__name']
    ordering_fields = ['price']