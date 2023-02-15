# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       Serializers allow complex data such as querysets and model instances to be converted to 
#       native Python datatypes that can then be easily rendered into JSON, XML or other content types. 
#
#       Ref: https://www.django-rest-framework.org/api-guide/serializers/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 15-Feb-2023  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================

from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')
