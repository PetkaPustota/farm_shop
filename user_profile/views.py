from django.http import Http404
from rest_framework import permissions, status
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from user_profile.permissions import ProfileUserPermission
from user_profile.models import ProfileUser
from user_profile.serializers import ProfileSerializer


class Profile(RetrieveUpdateAPIView):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, ProfileUserPermission)
    lookup_field = 'user_id'


# class ProfileNew(APIView):
#     serializer_class = ProfileSerializer
#
#     def get(self, request):
#         user_id = request.user.pk
#         if user_id:
#             serializer = ProfileSerializer(Profile.objects.get(user_id=user_id))
#             Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             raise Http404("Profile not found")
#
#     def patch(self, request):
#         user_id = request.user.pk
#         if user_id:
#             content = request.data
