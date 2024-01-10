from api.views import ProductListView
from api.spectacular.urls import urlpatterns as doc_path
from user_profile.views import Profile
from django.urls import path

urlpatterns = [
    path('products/', ProductListView.as_view()),
]

urlpatterns += doc_path
