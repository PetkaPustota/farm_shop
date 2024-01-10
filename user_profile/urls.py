from user_profile.views import Profile
from django.urls import path

urlpatterns = [
    path('profile/<int:user_id>', Profile.as_view()),
]
