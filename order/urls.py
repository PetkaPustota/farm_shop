from order.views import OrderView
from user_profile.views import Profile
from django.urls import path

urlpatterns = [
    path('orders/create/', OrderView.as_view()),
]
