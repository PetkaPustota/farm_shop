from rest_framework import serializers
from user_profile.models import ProfileUser
from phonenumber_field.serializerfields import PhoneNumberField
from phonenumber_field.validators import validate_international_phonenumber


class ProfileSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    phone = PhoneNumberField(region="RU", required=False)

    class Meta:
        model = ProfileUser
        fields = ['user_id', 'first_name', 'last_name', 'address', 'phone']

    # def to_representation(self, instance):
    #     self.user_id = self.context['user']
    #     return super().to_representation(instance)

    def is_valid(self, raise_exception=False):
        self._phone = self.initial_data.pop('phone', None)
        if self._phone is not None:
            validate_international_phonenumber(self._phone)
        else:
            raise serializers.ValidationError("not null")
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        profile = super().save()
        profile.phone = self._phone
        profile.save()
        return profile
