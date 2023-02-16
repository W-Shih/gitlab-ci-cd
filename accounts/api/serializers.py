# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       - Serializers allow complex data such as querysets and model instances to be converted to
#         native Python datatypes that can then be easily rendered into JSON, XML or other content
#         types.
#       - Can be used as a validator to validate if request is valid
#
#       Ref: https://www.django-rest-framework.org/api-guide/serializers/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 15-Feb-2023  Wayne Shih              Initial create
# 16-Feb-2023  Wayne Shih              Add LoginSerializer and SignupSerializer
# $HISTORY$
# =================================================================================================


from django.contrib.auth.models import User
from rest_framework import serializers, exceptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


# <Wayne Shih> 16-Feb-2023
# Ref: https://www.django-rest-framework.org/api-guide/serializers/#field-level-validatio
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


# <Wayne Shih> 16-Feb-2023
# Deriving from ModelSerializer to create/update a data when save() is called.
class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, min_length=6)
    password = serializers.CharField(max_length=20, min_length=6)
    email = serializers.EmailField()

    # <Wayne Shih> 16-Feb-2023
    # Assign User model and fields.
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    # <Wayne Shih> 16-Feb-2023
    # Will be called when is_valid is called.
    # Default validate() only checks if exact the same.
    # We overwrite this method to make it not case-sensitive.
    def validate(self, data):
        if User.objects.filter(username=data['username'].lower()).exists():
            raise exceptions.ValidationError({
                'message': 'This username has been occupied.'
            })
        if User.objects.filter(email=data['email'].lower()).exists():
            raise exceptions.ValidationError({
                'message': 'This email address has been occupied.'
            })
        return data

    # <Wayne Shih> 16-Feb-2023
    # Need to implement create() method, which is an abstract method.
    # Will be called save() is called.
    # To create a user, underneath we save all lower cases for username and email
    # in order to make validation efficient.
    def create(self, validated_data):
        username = validated_data['username'].lower()
        email = validated_data['email'].lower()
        password = validated_data['password']

        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
